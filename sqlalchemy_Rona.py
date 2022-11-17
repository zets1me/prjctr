# -- 1. Add models for student, subject and student_subject from previous lessons in SQLAlchemy.
# -- 2. Find all students` name that visited 'English' classes

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Student_Table(Base):
    __tablename__ = 'student_table'

    student_id = Column (Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    english_classes = relationship(
        "Student_subject_table",
        primaryjoin="and_(Student.student_id==Student_subject_table.student_id, " "Student_subject_table.subject_id==1)",
    )

class Subject_Table(Base):
    __tablename__ = 'student_subject'

    subject_id = Column (Integer, primary_key=True)
    subject_name = Column (String)

class Student_subject_table(Base):
    __tablename__ = 'student_subject_table'

    student_id = Column(Integer, ForeignKey=Student_Table)
    subject_id = Column(Integer, ForeignKey=Subject_Table)
    student_subject_id = Column(Integer, primary_key=True)


session.query(Student_Table).filter(Student_Table.subject_id == 1).all()