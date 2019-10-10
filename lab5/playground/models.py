from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class course(db.Model):
    __tablename__ = "course"
    course_id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String, nullable=False)
    course_title = db.Column(db.String, nullable=False)

    Students = db.relationship("student", backref="Courses", lazy=True)

    def add_student(self, name, grade):
        new_student = student(name=name, grade=grade)
        db.session.add(new_student)
        db.session.commit()


class student(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
