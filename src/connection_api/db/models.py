from enum import Enum as PyEnum

from sqlalchemy import (Column, DateTime, Enum, Float, ForeignKey, Integer,
                        String, Table)
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.connection_api.db.base import Base


class CategoryDifficulty(PyEnum):
    YELLOW = 1
    GREEN = 2
    BLUE = 3
    PURPLE = 4

puzzle_category_association = Table(
    "puzzle_category_association",
    Base.metadata,
    Column("puzzle_id", ForeignKey("puzzles.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
    Column("display_order", Integer)
)


class Puzzle(Base, AsyncAttrs):
    """Represents a complete Connections puzzle"""
    __tablename__ = "puzzles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    difficulty = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(String(20), nullable=False)
    author = Column(String(100))

    categories = relationship(
        "Category",
        secondary=puzzle_category_association,
        back_populates="puzzles"
    )
    items = relationship("Item", back_populates="puzzle")
    attempts = relationship("Attempt", back_populates="puzzle")


class Category(Base, AsyncAttrs):
    """Represents an individual word/item that belongs to a category"""
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    difficulty = Column(Enum(CategoryDifficulty), nullable=False)

    puzzles = relationship(
        "Puzzle",
        secondary=puzzle_category_association,
        back_populates="categories"
    )
    items = relationship("Item", back_populates="category")


class Item(Base, AsyncAttrs):
    """Represents an individual word/item that beongs to a category"""
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(50), nullable=False, unique=True)
    puzzle_id = Column(Integer, ForeignKey("puzzles.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    puzzle = relationship("Puzzle", back_populates="items")
    category = relationship("Category", back_populates="items")


class Solution(Base, AsyncAttrs):
    __tablename__ = "solutions"

    id = Column(Integer, primary_key=True, index=True)
    puzzle_id = Column(Integer, ForeignKey("puzzles.id"))
    player_id = Column(String(100))

    total_guesses = Column(Integer, nullable=False)
    correct_guess_order = Column(String(50))
    time_spent_seconds = Column(Float)

    started_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True))

    puzzles = relationship("Puzzle", back_populates="solutions")
