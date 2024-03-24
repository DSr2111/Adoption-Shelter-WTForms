from flask import flask
from flask_debugtoolbar import DebugToolBarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345as'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

connect_db(app)
db.create_all()


@app.route("/")
def list_pets():
    """List all pets up for adoption"""

    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add pet to agency"""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))

    else:
        # re-present form for editing
        return render_template("pet_add_form.html", form=form)