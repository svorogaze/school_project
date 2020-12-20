from flask import Flask, render_template

app = Flask(__name__)
dict_grades = {}
file = open('grades.txt', 'r', encoding='utf-8')
for i in file.readlines():
    splitted = i.split()
    dict_grades[splitted[0]] = splitted[1:]


@app.route('/')
def home():
    return render_template('proekt.html', gd=dict_grades)


app.run()
