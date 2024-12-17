from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Course(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
