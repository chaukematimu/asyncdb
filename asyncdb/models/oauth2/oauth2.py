from typing import TYPE_CHECKING, List, Optional

from pydantic.types import UUID4
from sqlalchemy.sql.schema import Column
from sqlmodel import ARRAY, String
from sqlmodel.main import Field, Relationship
from asyncdb.models.base import DatabaseModel

if TYPE_CHECKING:  # pragma: no cover
    from asyncdb.models.oauth2.users import User


class Client(DatabaseModel, table=True):  # type: ignore
    __tablename__ = "clients"

    client_id: str
    client_secret: str
    grant_types: List[str] = Field(sa_column=Column(ARRAY(String)))
    response_types: List[str] = Field(sa_column=Column(ARRAY(String)))
    redirect_uris: List[str] = Field(sa_column=Column(ARRAY(String)))

    scope: str

    user_id: UUID4 = Field(foreign_key="users.id", nullable=False)
    user: "User" = Relationship(back_populates="user_clients")


class AuthorizationCode(DatabaseModel, table=True):  # type: ignore
    __tablename__ = "authorization_codes"

    code: str
    client_id: str
    redirect_uri: str
    response_type: str
    scope: str
    auth_time: int
    expires_in: int
    code_challenge: Optional[str]
    code_challenge_method: Optional[str]
    nonce: Optional[str]

    user_id: UUID4 = Field(foreign_key="users.id", nullable=False)
    user: "User" = Relationship(back_populates="user_authorization_codes")


class Token(DatabaseModel, table=True):  # type: ignore
    __tablename__ = "tokens"

    access_token: str
    refresh_token: str
    scope: str
    issued_at: int
    expires_in: int
    refresh_token_expires_in: int
    client_id: str
    token_type: str
    revoked: bool

    user_id: UUID4 = Field(foreign_key="users.id", nullable=False)
    user: "User" = Relationship(back_populates="user_tokens")