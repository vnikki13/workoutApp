from typing import List
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from workout_app import db
from workout_app import app
from workout_app import Base
from datetime import datetime

# class User(db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     first_name: Mapped[str] = mapped_column(String(40), nullable=False)
#     last_name: Mapped[str] = mapped_column(String(60), nullable=False)
#     email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
#     password: Mapped[str] = mapped_column(String(60), nullable=False)
#     workouts: Mapped[List["Workout"]] = relationship(back_populates="user", cascade="all, delete-orphan")
#     exercises: Mapped[List["Exercise"]] = relationship(back_populates="user", cascade="all, delete-orphan")

#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}), workouts={self.workouts!r}, exercises={self.exercises!r}"

class Exercise(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    summary: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    equipment: Mapped[str] = mapped_column()
    date_created: Mapped[datetime] = mapped_column(db.DateTime, nullable=False, default=datetime.utcnow)
    workouts: Mapped[List["Workout"]] = relationship(secondary="exercise_to_workout_table", back_populates="exercises")
    # user: Mapped["User"] = relationship(back_populates="exercises")

class Workout(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    exercises: Mapped[List["Exercise"]] = relationship(secondary="exercise_to_workout_table", back_populates="workouts")
    # user: Mapped["User"] = relationship(back_populates="workouts")

exercise_to_workout_table = db.Table(
    "exercise_to_workout_table",
    Column("exercise_id", ForeignKey(Exercise.id), primary_key=True),
    Column("workout_id", ForeignKey(Workout.id), primary_key=True),
)

with app.app_context():
    db.create_all()
    db.session.commit()
