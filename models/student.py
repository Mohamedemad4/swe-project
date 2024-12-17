from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Student(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]= mapped_column()


    '''
    name
    id
    email
    courses[]


    course>> name
    student
    grades 


    grades
    course id
    student id
    grade

    '''