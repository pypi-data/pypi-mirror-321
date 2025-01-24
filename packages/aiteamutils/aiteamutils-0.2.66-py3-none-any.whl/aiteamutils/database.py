#기본 라이브러리
from typing import TypeVar, Generic, Type, Any, Dict, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

#패키지 라이브러리
from .exceptions import ErrorCode, CustomException


ModelType = TypeVar("ModelType", bound=DeclarativeBase)

##################
# 전처리 #
##################



##################
# 응답 처리 #
##################
def process_columns(
        entity: ModelType,
        exclude_extra_data: bool = True
) -> Dict[str, Any]:
    """엔티티의 컬럼들을 처리합니다.

    Args:
        entity (ModelType): 처리할 엔티티
        exclude_extra_data (bool, optional): extra_data 컬럼 제외 여부. Defaults to True.

    Returns:
        Dict[str, Any]: 처리된 컬럼 데이터
    """
    result = {}
    for column in entity.__table__.columns:
        if exclude_extra_data and column.name == 'extra_data':
            continue
            
        # 필드 값 처리
        if hasattr(entity, column.name):
            value = getattr(entity, column.name)
            if isinstance(value, datetime):
                value = value.isoformat()
            result[column.name] = value
        elif hasattr(entity, 'extra_data') and isinstance(entity.extra_data, dict):
            result[column.name] = entity.extra_data.get(column.name)
        else:
            result[column.name] = None
    
    # extra_data의 내용을 최상위 레벨로 업데이트
    if hasattr(entity, 'extra_data') and isinstance(entity.extra_data, dict):
        result.update(entity.extra_data or {})
            
    return result

def process_response(
        entity: ModelType,
        response_model: Any = None
) -> Dict[str, Any]:
    """응답 데이터를 처리합니다.
    extra_data의 내용을 최상위 레벨로 변환하고, 라우터에서 선언한 응답 스키마에 맞게 데이터를 변환합니다.

    Args:
        entity (ModelType): 처리할 엔티티
        response_model (Any, optional): 응답 스키마. Defaults to None.

    Returns:
        Dict[str, Any]: 처리된 엔티티 데이터
    """
    if not entity:
        return None

    # 모든 필드 처리
    result = process_columns(entity)
    
    # Relationship 처리 (이미 로드된 관계만 처리)
    for relationship in entity.__mapper__.relationships:
        if not relationship.key in entity.__dict__:
            continue
            
        try:
            value = getattr(entity, relationship.key)
            # response_model이 있는 경우 해당 필드의 annotation type을 가져옴
            nested_response_model = None
            if response_model and relationship.key in response_model.model_fields:
                field_info = response_model.model_fields[relationship.key]
                nested_response_model = field_info.annotation
            
            if value is not None:
                if isinstance(value, list):
                    result[relationship.key] = [
                        process_response(item, nested_response_model)
                        for item in value
                    ]
                else:
                    result[relationship.key] = process_response(value, nested_response_model)
            else:
                result[relationship.key] = None
        except Exception:
            result[relationship.key] = None

    # response_model이 있는 경우 필터링
    if response_model:
        # 현재 키 목록을 저장
        current_keys = list(result.keys())
        # response_model에 없는 키 제거
        for key in current_keys:
            if key not in response_model.model_fields:
                result.pop(key)
        # 모델 검증 및 업데이트
        result.update(response_model(**result).model_dump())
            
    return result


##################
# 조건 처리 #
##################
def build_search_filters(
        request: Dict[str, Any],
        search_params: Dict[str, Dict[str, Any]]
) -> Dict[str, Any]:
    """
    요청 데이터와 검색 파라미터를 기반으로 필터 조건을 생성합니다.

    Args:
        request: 요청 데이터 (key-value 형태).
        search_params: 검색 조건 설정을 위한 파라미터.

    Returns:
        filters: 필터 조건 딕셔너리.
    """
    filters = {}
    for key, param in search_params.items():
        value = request.get(key)
        if value is not None:
            if param["like"]:
                filters[key] = {"field": param["fields"][0], "operator": "like", "value": f"%{value}%"}
            else:
                filters[key] = {"field": param["fields"][0], "operator": "eq", "value": value}
    return filters

def build_conditions(
        filters: Dict[str, Any],
        model: Type[ModelType]
) -> List[Any]:
    """
    필터 조건을 기반으로 SQLAlchemy 조건 리스트를 생성합니다.

    Args:
        filters: 필터 조건 딕셔너리.
        model: SQLAlchemy 모델 클래스.

    Returns:
        List[Any]: SQLAlchemy 조건 리스트.
    """
    conditions = []
    for filter_data in filters.values():
        if "." in filter_data["field"]:
            # 관계를 따라 암묵적으로 연결된 모델의 필드 가져오기
            related_model_name, field_name = filter_data["field"].split(".")
            relationship_property = getattr(model, related_model_name)
            related_model = relationship_property.property.mapper.class_
            field = getattr(related_model, field_name)
        else:
            # 현재 모델의 필드 가져오기
            field = getattr(model, filter_data["field"])

        # 조건 생성
        operator = filter_data["operator"]
        value = filter_data["value"]

        if operator == "like":
            conditions.append(field.ilike(f"%{value}%"))
        elif operator == "eq":
            conditions.append(field == value)

    return conditions

##################
# 쿼리 실행 #
##################
async def list_entities(
    session: AsyncSession,
    model: Type[ModelType],
    skip: int = 0,
    limit: int = 100,
    filters: Optional[Dict[str, Any]] = None,
    joins: Optional[List[Any]] = None
) -> List[Dict[str, Any]]:
    """
    엔터티 리스트를 필터 및 조건에 따라 가져오는 함수.

    Args:
        session: SQLAlchemy AsyncSession.
        model: SQLAlchemy 모델.
        skip: 페이지네이션 시작 위치.
        limit: 페이지네이션 크기.
        filters: 필터 조건 딕셔너리.
            예시:
            filters = {
                "search": {"field": "username", "operator": "like", "value": "%admin%"},
                "name": {"field": "name", "operator": "like", "value": "%John%"},
                "role_ulid": {"field": "role_ulid", "operator": "eq", "value": "1234"}
            }

        joins: 조인 옵션.
            예시:
            joins = [
                selectinload(YourModel.related_field),  # 관련된 필드를 함께 로드
                joinedload(YourModel.another_related_field)  # 다른 관계된 필드를 조인
            ]

    Returns:
        List[Dict[str, Any]]: 쿼리 결과 리스트.
    """
    try:
        query = select(model)

        # 필터 조건 적용
        if filters:
            conditions = build_conditions(filters, model)
            query = query.where(and_(*conditions))

        # 조인 로딩 적용
        if joins:
            for join_option in joins:
                query = query.options(join_option)

        # 페이지네이션 적용
        query = query.limit(limit).offset(skip)

        result = await session.execute(query)
        return result.scalars().unique().all()
    except SQLAlchemyError as e:
        raise CustomException(
            ErrorCode.DB_READ_ERROR,
            detail=f"{model.__name__}|{str(e)}",
            source_function="database.list_entities",
            original_error=e
        )
