from sqlmodel import Field, SQLModel


class UsuarioCreate(SQLModel):
    username: str = Field(min_length=3, max_length=50)
    mail: str = Field(max_length=100)
    password: str = Field(min_length=8)


class Token(SQLModel):
    access_token: str
    token_type: str
