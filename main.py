from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# app = Flask(__name__)
# app.config[''] = ''
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# app.config['SQLALCHEMY_DATABASE_url'] = 'sqlite://blog.db'
# db = SQLAlchemy(app)

#
# class LoginForm(FlaskForm):
#     username = StringField('Логин', validators=[DataRequired()])
#     password = PasswordField('Пароль', validators=[DataRequired()])
#     remember_me = BooleanField('Запомнить меня')
#     submit = SubmitField('Войти')
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('login.html', title='Авторизация', form=form)
# @app.route("/<title>")
# @app.route("/index/<title>")
# def index(title):
#     return render_template("index.html", title=title)


# @app.route("/base")
# def base():
#     return render_template("base.html")

#
# @app.route("/home")
# def home():
#     return render_template("home.html")
#
#
# @app.route("/request")
# def request():
#     return render_template("request.html")
#
#
# @app.route("/sc")
# def sc():
#     return render_template("sc.html")
#
#
# @app.route("/warehouse")
# def warehouse():
#     return render_template("warehouse.html")
#
#
# @app.route("/warehouseSc")
# def warehousesc():
#     return render_template("warehouseSc.html")
#
#
# @app.route("/delivery warehouse")
# def dwarehouse():
#     return render_template("delivery warehouse.html")
#
#
# @app.route("/log")
# def log():
#     return render_template("log.html")
#
#
# @app.route("/statistics")
# def statistics():
#     return render_template("statistics.html")
#
#
# @app.route("/profile")
# def profile():
#     return render_template("profile.html")
#
#
# @app.route("/base")
# def base():
#     return render_template("base.html")
#
# if __name__ == "__main__":
#     app.run(port=666, host='127.0.0.1')
#


# @app.route("/about")
# def about():
#     return render_template("about.html", number=5)
#
#
# @app.route("/training/<prof>")
# def train(prof):
#     return render_template("training.html", profession=prof)

#
# if __name__ == "__main__":
#     app.run(port=666, host='127.0.0.1')

# @app.route("about")
# def about(title):
#     return render_template("about.html", title=title)
#
# @app.route("/base")
# def base():
#     return render_template("base.html")

from flask import Flask
from data import db_session
from data.news import News
from data.users import User
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/index/home')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/index/home")
def home():
    return render_template("home.html")


@app.route("/index/request")
def request():
    return render_template("request.html")


@app.route("/index/sc")
def sc():
    return render_template("sc.html")


@app.route("/index/warehouse")
def warehouse():
    return render_template("warehouse.html")


@app.route("/index/log")
def log():
    return render_template("log.html")


@app.route("/index/statistics")
def statistics():
    return render_template("statistics.html")


@app.route("/index/profile")
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    main()