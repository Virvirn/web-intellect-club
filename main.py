from flask import Flask, render_template, request, redirect
from data import db_session
import os
from data.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/registration_for_the_course', methods=['GET', 'POST'])
def course():
    db_session.global_init("db/course.db")
    db_sess = db_session.create_session()
    if request.method == 'POST':
        name = request.form['Username']
        phone = request.form['number_phone']
        age = request.form['age']
        courses = request.form['course']
        user = User(name=name, phone=phone, age=age, course=courses)

        try:
            db_sess.add(user)
            db_sess.commit()
            print('Данные были добавлены')
            return redirect('/registration_for_the_course')
        except:
            return 'Произошла ошибка'
    else:
        return render_template('index_2page.html')


@app.route('/information_about_the_organization')
def infor():
    return render_template('index_3.1page.html')


@app.route('/documents')
def doc():
    return render_template('index_3.2page.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
