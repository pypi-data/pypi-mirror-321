#기본 라이브러리
from typing import TypeVar, Generic, Type, Any, Dict, List, Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

#패키지 라이브러리
from .exceptions import ErrorCode, CustomException
from .database import list_entities

ModelType = TypeVar("ModelType", bound=DeclarativeBase)

class BaseRepository(Generic[ModelType]):
    def __init__(self, session: AsyncSession, model: Type[ModelType]):
        self._session = session
        self.model = model
    
    @property
    def session(self) -> AsyncSession:
        return self._session
    
    @session.setter
    def session(self, value: AsyncSession):
        if value is None:
            raise CustomException(
                ErrorCode.DB_CONNECTION_ERROR,
                detail="Session cannot be None",
                source_function=f"{self.__class__.__name__}.session"
            )
        self._session = value
    
    async def list(
        self,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[Dict[str, Any]] = None,
        joins: Optional[List[Any]] = None,
    ) -> List[ModelType]:
        """
        엔티티 목록 조회.
        """
        # 기본 CRUD 작업 호출
        return await list_entities(
            session=self.session,
            model=self.model,
            skip=skip,
            limit=limit,
            filters=filters,
            joins=joins,
        )
