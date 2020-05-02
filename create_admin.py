from getpass import getpass # скрытие поля с паролем от стороннего наблюдателя
import sys # модуль для взаимодействия с системными функциями, для корректного завершения функций

from webapp import create_app
from webapp.db import db
from webapp.user.models import User
from datetime import datetime

app = create_app()

with app.app_context(): # строка после которой можно работать с базой данных
    user_email = input('Your email address: ')

    if User.query.filter(User.user_email == user_email).count():
        print('A user with the same name already exists.')
        sys.exit(0)

    password = getpass('Password: ')
    password2 = getpass('Repeat password: ')
    if not password == password2:
        print("Passwords don't match.")
        sys.exit(0)

    date_now = datetime.now()
    date_reg = date_now.strftime('%d.%m.%Y')
    picture_user = input('Write the name of the avatar:')
    username = input('Write a nickname:')

    new_user = User(user_email=user_email, role='admin', date_reg=date_reg, picture=picture_user, username=username)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('User with id={} added'.format(new_user.id))