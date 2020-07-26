from lib.dtos.DeclarativeBaseContainer import *


class StudentResult(Base):
    def __int__(self, id=None, res_path=None, student_id=None, semester_id=None):
        self.id = id
        self.res_path = res_path
        self.student_id = student_id
        self.semester_id = semester_id

    __tablename__ = 'student_results'
    id = Column(String, primary_key=True)
    res_path = Column(String)

    student_id = Column(String, ForeignKey('students.id'), nullable=True)
    # student = relationship('lib.dtos.Student.Student', back_populates="results")

    semester_id = Column(String, ForeignKey('semesters.id'), nullable=True)
    # semester = relationship('lib.dtos.Semester.Semester')
