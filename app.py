from flask import Flask, render_template, request, redirect
from repositories.studentsRepository import StudentsRepository
app = Flask(__name__)

StudentsRepo = StudentsRepository()

# Homepage to view students
@app.route('/')
def index():
    return render_template('index.html', students=StudentsRepo.students)

# Add a new student
@app.route('/add-student', methods=['POST'])
def add_student():
    StudentsRepo.add(request.form['name'],request.form['student_id'],request.form['course_ids'])
    return redirect('/')


# Run the application
if __name__ == '__main__':
    app.run(debug=True)