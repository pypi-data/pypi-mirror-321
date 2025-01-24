#기본 라이브러리
from fastapi import Request
from typing import TypeVar, Generic, Type, Dict, Any, Union, List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
#패키지 라이브러리
from .exceptions import ErrorCode, CustomException
from .base_repository import BaseRepository

ModelType = TypeVar("ModelType", bound=DeclarativeBase)

class BaseService(Generic[ModelType]):
    ##################
    # 1. 초기화 영역 #
    ##################
    def __init__(
            self,
            model: Type[ModelType],
            repository: BaseRepository[ModelType],
            db_session: AsyncSession
    ):
        self.model = model
        self.repository = repository
        self.db_session = db_session

    async def list(
        self,
        skip: int = 0,
        limit: int = 100,
        filters: Dict[str, Any] | None = None,
        search_params: Dict[str, Any] | None = None,
        model_name: str | None = None,
    ) -> List[Dict[str, Any]]:
        try:
            # 모델 이름을 통한 동적 처리
            if model_name:
                if model_name not in self.additional_models:
                    raise CustomException(
                        ErrorCode.INVALID_REQUEST,
                        detail=f"Model {model_name} not registered",
                        source_function=f"{self.__class__.__name__}.list"
                    )
                model = self.additional_models[model_name]
                return await self.repository.list(skip=skip, limit=limit, filters=filters, model=model)

            return await self.repository.list(skip=skip, limit=limit, filters=filters)
        except CustomException as e:
            e.detail = f"Service list error for {self.repository.model.__tablename__}: {e.detail}"
            e.source_function = f"{self.__class__.__name__}.list -> {e.source_function}"
            raise e
        except Exception as e:
            raise CustomException(
                ErrorCode.INTERNAL_ERROR,
                detail=str(e),
                source_function=f"{self.__class__.__name__}.list",
                original_error=e
            )


