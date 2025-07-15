from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import relationship
from src.connection_api.db.base import Base


class Puzzle(Base, AsyncAttrs):
    __tablename__ = "puzzles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    difficulty = Column(Integer)

    groups = relationship("Group", back_populates="puzzle")


class Group(Base, AsyncAttrs):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    puzzle_id = Column(Integer, ForeignKey("puzzles.id"))
    name = Column(String, nullable=False)
    description = Column(String)

    puzzle = relationship("Puzzle", back_populates="groups")
    items = relationship("Item", back_populates="group")


class Item(Base, AsyncAttrs):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    text = Column(String, nullable=False)

    group = relationship("Group", back_populates="items")
