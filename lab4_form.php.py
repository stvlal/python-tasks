#todo:
# Необходимо разработать форму ввода тестовых вопросов пользователем в конструкторе форм https://beautifytools.com/html-form-builder.php
# Прикрутить форму к flask. Отдать флому  через шаблонизатор Jinja.
# При заполнении и отправки данных на сервер валидировать их и записать через модель ORM в PostgresSQL

from flask import Flask
from flask import render_template
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy

DB_NAME = 'site_users'
USERNAME = 'postgres'
PASSWORD = 'postgres'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USERNAME}:{PASSWORD}@localhost:5432/{DB_NAME}'

db = SQLAlchemy()
db.init_app(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return f'{self.id}'


with app.app_context():
    db.create_all()


def check_username(username):
    if len(username) > 8:
        return False
    else:
        return True


@app.route("/")
@app.route("/index")
def greeting():
    return render_template("index.html", title='Hello', header='Как с этим работать?')


@app.route('/user/<username>')
def show_user_profile(username):
    if not check_username(escape(username)):
        return render_template("index.html", title='Hello', header='Требования к username внизу')
    user = Users.query.filter_by(name=escape(username)).first()
    if user:
        user_id = user
        comment = 'is in the database and has'
    else:
        db.session.add(Users(name=escape(username)))
        db.session.commit()
        user = Users.query.filter_by(name=escape(username)).first()
        user_id = user
        comment = 'has been created with'

    return render_template("userinfo.html",
                           username=escape(username),
                           comment=comment,
                           id=user_id)


app.run()
