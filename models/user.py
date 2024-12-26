from .database import db
from sqlalchemy import Integer, String, Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Association table remains the same but renamed for clarity
user_course = Table(
    "user_course",
    db.Model.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("course_id", ForeignKey("course.id"), primary_key=True),
)

class User(db.Model):
    __tablename__ = 'user'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column()
    user_type: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    
    # Move grades relationship to base User class
    grades: Mapped[list["Grade"]] = relationship(back_populates="student")
    
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': user_type
    }

class Student(User):
    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }
    
    # Student-specific relationships - only courses remains here
    courses: Mapped[list["Course"]] = relationship(
        secondary=user_course,
        back_populates="students"
    )

class Admin(User):
    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }
    
    # Admin-specific columns
    department: Mapped[str] = mapped_column(String, nullable=True)
    access_level: Mapped[int] = mapped_column(Integer, default=1) 