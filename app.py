from flask import flask
from flask_debugtoolbar import DebugToolBarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345as'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

connect_db(app)
db.createall()

