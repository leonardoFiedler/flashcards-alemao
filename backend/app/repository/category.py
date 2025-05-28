from typing import List
from sqlalchemy.orm import Session

from app.repository import models


def get_all_categories(session: Session) -> List[models.Category]:
    return session.query(models.Category).all()


def find_category_by_id(category_id: int, session: Session) -> models.Category:
    db_category = session.scalar(session.query(models.Category).where(
        models.Category.id == category_id
    ))

    if not db_category:
        raise models.RecordNotFoundException(f"Category {category_id} not found!")

    return db_category


def insert_category(name: str, session: Session) -> models.Category:
    db_category = models.Category(name=name)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category


def update_category(category_id: int, name: str, session: Session) -> models.Category:
    db_category = find_category_by_id(category_id, session)
    db_category.name = name
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category


def delete_category(category_id: int, session: Session):
    db_category = find_category_by_id(category_id, session)
    session.delete(db_category)
    session.commit()
