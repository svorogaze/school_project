from flask import Flask, render_template

app = Flask(__name__)
dict_grades = {}
file = open('grades.txt', 'r', encoding='utf-8')
for i in file.readlines():
    splitted = i.split()
    dict_grades[splitted[0]] = list(map(int,splitted[1:]))
sr_math = round(sum(dict_grades['математика']) / len(dict_grades['математика']), 1)
sr_russian = round(sum(dict_grades['математика']) / len(dict_grades['математика']), 1)


@app.route('/')
def home():
    return render_template('proekt.html', gd=dict_grades, sr_m=sr_math, sr_r=sr_russian)


if __name__ == '__main__':
    app.run()
