from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Alias kept for backward compatibility with code that imports BaseModel
BaseModel = Base
