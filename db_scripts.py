
from typing import List
from sqlalchemy import String, Boolean, Integer, create_engine
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase, mapped_column


from config import db, NUM

class Base(DeclarativeBase):
    pass

class Answer(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]  = mapped_column(String(100), nullable=True)
    questions: Mapped[List] = [mapped_column(Boolean, nullable=True, default=None) for i in range(20)]
    mark: Mapped[int]  = mapped_column(Integer)

def create_db():
    engine = create_engine(db, echo=True)

if __name__ == "__main__":
    create_db()