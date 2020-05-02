# импортируем модуль питона для удобной работы с файловой системой
import os
from datetime import timedelta

# выводит на печать адрес текущей папки
# print(os.path.abspath(os.path.dirname(__file__)))

# сохраняем в переменную адрес текущего каталога
basedir = os.path.abspath(os.path.dirname(__file__))

# добавляем в адрес текущей папки указание на рядом лежащие папки
# print(os.path.join(basedir, '..', 'webapp.db')

# указываем какой движок мы используем. в данном случае sqlite. Если будет postgres, то необходимо будет указать
# точку подключения к postgres через адрес доменного имени, порт, имя базы данных и т.д.
# sqlite:///

# адрес на жестком диске для базы
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = 'ehuiwevwevwbveu'

REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_TIME_LIMIT= None