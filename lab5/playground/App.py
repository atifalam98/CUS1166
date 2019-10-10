import sys
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

from lab5.playground.models import db, course, student

app = Flask(__name__)
app.config.from_object(Config)
app.app_context().push()
db.init_app(app)


@app.route('/')
def hello():
    courses = course.query.all()
    return render_template("index.html", courses=courses)

@app.route('/add_course', methods=["post"])
def add_course():
    course_number = request.form.get("course_number")
    course_title = request.form.get("course_title")
    new_course = course(course_number=course_number, course_title=course_title)
    db.session.add(new_course)
    db.session.commit()
    courses = course.query.all()
    return render_template('index.html', courses=courses)

@app.route('/course_details/<int:course_id>')
def course_students(course_id):
    students = student.query.all()
    return render_template("course_details.html", students=students, course_id=course_id)

@app.route('/add_student/<int:course_id>', methods=["post"])
def add_student(course_id):
    course_number = request.form.get("student_name")
    course_title = request.form.get("student_grade")
    new_student = student(name=course_number, grade=course_title, course_id=course_id)
    db.session.add(new_student)
    db.session.commit()
    students = student.query.all()
    return render_template('course_details.html', students=students, course_id=course_id)


def main():
    if len(sys.argv) == 2:
        print(sys.argv)
        if sys.argv[1] == 'It is created':
            db.create_all()
    else:
        app.run()

if __name__=='__main__':
    main()



