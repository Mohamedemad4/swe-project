from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class StudentCourse(db.Model):
    course_id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[str] = mapped_column(unique=True)
    