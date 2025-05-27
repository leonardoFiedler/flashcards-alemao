from typing import Any
from fastapi import APIRouter
from app.api.deps import SessionDep

from app.schemas import CategoriesPublic
from app.repository.category import get_all_categories


router = APIRouter(prefix="/categories", tags=["categories"])


@router.get(
    "/",
    response_model=CategoriesPublic,
)
def get_categories(session: SessionDep) -> Any:
    return get_all_categories(session)
