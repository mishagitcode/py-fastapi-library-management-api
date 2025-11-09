from datetime import date

from pydantic import BaseModel


class AuthorBase(BaseModel):
    id: int
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class AuthorList(AuthorBase):

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    id: int
    title: str
    summary: str
    publication_date: date
    author_id: int


class BookCreate(BookBase):
    pass


class BookList(BookBase):

    class Config:
        orm_mode = True
