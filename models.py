from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

class Pet(db.model):
    """Pet for adoption"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Getting assigned picture or generic one for pet"""

        return self.photo_url or GENERIC_IMAGE

def connect_db(app):
    """Connect database to app"""

    db.app = app
    db.init_app(app)