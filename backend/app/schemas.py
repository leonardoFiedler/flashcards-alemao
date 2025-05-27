from pydantic import BaseModel


class CreateCategory(BaseModel):
    name: str


class CategoryPublic(CreateCategory):
    id: int


class CategoriesPublic(BaseModel):
    data: list[CategoryPublic]
    count: int
