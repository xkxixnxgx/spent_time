from flask import Flask, render_template
from webapp.forms import LoginForm
# импортируем структуру базы данных
from webapp.model import db
from webapp.config import SECRET_KEY


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')


    @app.route('/login')
    def login():
        title = 'Sigh in'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    if __name__ == '__main__':
        app.run(debug=True)

    return app
