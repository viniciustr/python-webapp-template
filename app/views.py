from flask import Blueprint


views = Blueprint('views', __name__, template_folder='templates')


@views.route('/')
def hello_world():
    return 'Hello, World!'
