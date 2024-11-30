class StudentsRepository:
    def __init__(self):
        self.students = []

    def add(self,name,student_id,course_ids):
        student = {'name':name,'student_id':student_id,'course_ids':course_ids}
        self.students.append(student)
        return student