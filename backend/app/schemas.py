from pydantic import BaseModel


class Message(BaseModel):
    message: str


class CreateCategorySchema(BaseModel):
    name: str


class CategoryPublicSchema(CreateCategorySchema):
    id: int


class CategoriesPublicSchema(BaseModel):
    data: list[CategoryPublicSchema]
    count: int
