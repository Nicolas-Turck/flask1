# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
import os

SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
FB_APP_ID = 198000961272990


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
