from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/welcome/<string:student_name>')
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

@app.route('/roster/<int:view>')
def roster(view):
    class_roster=[{ 'name':"Sheldon", 'grade':100, 'year':"sophomore"},
            {'name':"Penny", 'grade':98, 'year':"sophomore"},
            {'name':"Leonard", 'grade':93, 'year':"junior"},
            {'name':"Howard", 'grade':87, 'year':"freshman"},
            {'name':"Raj", 'grade':85, 'year':"freshman"},
            {'name':"Amy", 'grade':91, 'year':"senior"},
            {'name':"Barry", 'grade':86, 'year':"junior"}]
    return render_template("roster.html", view=view, class_roster=class_roster)

if __name__ == '__main__':
    app.run(debug=True)