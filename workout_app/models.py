from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from workout_app import db
from workout_app import app
from datetime import datetime

class Exercise(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    summary: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    equipment: Mapped[str] = mapped_column()
    date_created: Mapped[datetime] = mapped_column(db.DateTime, nullable=False, default=datetime.utcnow)


with app.app_context():
    db.create_all()
    # db.session.add(Exercise(
    #     title="Chin up", 
    #     summary="Pull up with palms facing you", 
    #     description="Can be a hard exercise", 
    #     equipment='Rings'
    # ))
    db.session.commit()
