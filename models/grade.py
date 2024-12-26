from .database import db
from sqlalchemy import Integer, String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Grade(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    grade: Mapped[float] = mapped_column(Float)
    
    # Foreign keys
    student_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"), nullable=False)
    
    # Relationships
    student: Mapped["User"] = relationship("User", back_populates="grades")
    course: Mapped["Course"] = relationship("Course", back_populates="grades") 