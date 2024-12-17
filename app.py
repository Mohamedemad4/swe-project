from flask import Flask, render_template, request, redirect
from repositories.studentsRepository import StudentsRepository
from models.database import db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

StudentsRepo = StudentsRepository()

# Homepage to view students
@app.route('/')
def index():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template('index.html', students=StudentsRepo.students)
    
# Add a new student
@app.route('/add-student', methods=['POST'])
def add_student():
    StudentsRepo.add(request.form['name'],request.form['student_id'],request.form['course_ids'])
    return redirect('/')


# Run the application
if __name__ == '__main__':
    app.run(debug=True)