#기본 라이브러리
from typing import TypeVar, Generic, Type, Any, Dict, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.exc import SQLAlchemyError

ModelType = TypeVar("ModelType", bound=DeclarativeBase)

#패키지 라이브러리
from .exceptions import ErrorCode, CustomException

##################
# 1. 쿼리 실행 #
##################
async def list_entities(
    session: AsyncSession,
    model: Type[ModelType],
    skip: int = 0,
    limit: int = 100,
    filters: Optional[Dict[str, Any]] = None,
    joins: Optional[List[Any]] = None
) -> List[Dict[str, Any]]:
    try:
        query = select(model)

        # 필터 조건 적용
        if filters:
            conditions = [getattr(model, key) == value for key, value in filters.items()]
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
