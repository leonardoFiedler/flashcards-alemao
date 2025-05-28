from http import HTTPStatus
from typing import Any
from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep

from app.schemas import (
    CategoriesPublicSchema,
    CategoryPublicSchema,
    CreateCategorySchema,
    Message,
)
from app.repository.category import (
    delete_category,
    get_all_categories,
    insert_category,
    update_category,
)
from app.repository.models import RecordNotFoundException



router = APIRouter(prefix="/categories", tags=["categories"])


@router.get(
    "/",
    response_model=CategoriesPublicSchema,
)
def list_categories(session: SessionDep) -> Any:
    categories = get_all_categories(session)
    return {"data": categories, "count": len(categories)}


@router.post(
    "/",
    response_model=CategoryPublicSchema,
)
def create_category(category: CreateCategorySchema, session: SessionDep) -> Any:
    category = insert_category(category.name, session)

    return {"id": category.id, "name": category.name}


@router.patch(
    "/{category_id}",
    response_model=CategoryPublicSchema,
)
def patch_category(
    category_id: int, category: CreateCategorySchema, session: SessionDep
) -> Any:
    try:
        category = update_category(category_id, category.name, session)
    except RecordNotFoundException as e:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail=str(e)
        )
    
    return {"id": category.id, "name": category.name}


@router.delete("/{category_id}", response_model=Message)
async def delete_todo(category_id: int, session: SessionDep):
    try:
        delete_category(category_id, session)
    except RecordNotFoundException as e:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail=str(e)
        )

    return {"message": "Category has been deleted successfully."}
