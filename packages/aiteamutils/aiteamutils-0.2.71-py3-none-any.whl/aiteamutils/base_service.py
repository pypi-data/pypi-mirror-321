#기본 라이브러리
from fastapi import Request
from typing import TypeVar, Generic, Type, Dict, Any, Union, List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

#패키지 라이브러리
from .exceptions import ErrorCode, CustomException
from .base_repository import BaseRepository
from .database import (
    process_response,
    build_search_filters
)

ModelType = TypeVar("ModelType", bound=DeclarativeBase)

class BaseService(Generic[ModelType]):
    ##################
    # 1. 초기화 영역 #
    ##################
    def __init__(
            self,
            model: Type[ModelType],
            repository: BaseRepository[ModelType],
            db_session: AsyncSession,
            additional_models: Dict[str, Type[DeclarativeBase]] = None,
    ):
        self.model = model
        self.repository = repository
        self.db_session = db_session
        self.additional_models = additional_models or {},

    async def list(
        self,
        skip: int = 0,
        limit: int = 100,
        filters: Dict[str, Any] | None =
        except Exception as e:
            raise CustomException(
                ErrorCode.INTERNAL_ERROR,
                detail=str(e),
                source_function=f"{self.__class__.__name__}.list",
                original_error=e
            )


