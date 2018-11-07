from flask import Flask
from flask_turbolinks import turbolinks

from views import views


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.register_blueprint(views)

turbolinks(app)
