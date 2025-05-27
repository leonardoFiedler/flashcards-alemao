from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "category"

    id = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    timestamp: Mapped[datetime] = mapped_column(insert_default=func.now())

    flashcards: Mapped[List["Flashcard"]] = relationship(back_populates="category")


class WordType(Base):
    __tablename__ = "word_type"

    id = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    timestamp: Mapped[datetime] = mapped_column(insert_default=func.now())

    flashcards: Mapped[List["Flashcard"]] = relationship(back_populates="word_type")


class Flashcard(Base):
    __tablename__ = "flashcard"

    id = mapped_column(Integer, primary_key=True)
    id_category = mapped_column(ForeignKey("category.id"))
    id_word_type = mapped_column(ForeignKey("word_type.id"))
    ge_translation: Mapped[str] = mapped_column(String(300))
    pt_translation: Mapped[str] = mapped_column(String(300))
    image_path: Mapped[str] = mapped_column(String(500))
    tip: Mapped[str] = mapped_column(String(500))
    article: Mapped[str] = mapped_column(String(8))
    plural: Mapped[str] = mapped_column(String(300))
    plural_options: Mapped[str] = mapped_column(String(500))

    category: Mapped["Category"] = relationship(back_populates="flashcards")
    word_type: Mapped["WordType"] = relationship(back_populates="flashcards")
