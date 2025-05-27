from typing import List
from sqlalchemy.orm import Session

from app.repository import models


def get_all_categories(db: Session) -> List[models.Category]:
    return db.query(models.Category).all()
