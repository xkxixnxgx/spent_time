from flask import Flask, render_template
# импортируем структуру базы данных
from webapp.model import db

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

    if __name__ == '__main__':
        app.run(debug=True)

    return app
