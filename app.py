from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SECRET!"

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def redirect_homepage():
    return redirect('/homepage')


@app.route('/homepage')
def homepage():
    """Displays the homepage"""
    pets = Pet.query.all()
    return render_template('/homepage.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add():
    """This route is both for displaying the add pet form and receiving that form's data which it sends
    to the database."""
    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet()
        pet.submit_pet(form)
        return redirect("/homepage")
    else:
        return render_template('/add.html', form=form)

@app.route('/<petId>')
def pet_page(petId):
    pet = Pet.query.get_or_404(petId)
    return render_template('/pet.html', pet=pet)

@app.route('/<int:id>/adopt', methods=["POST"])
def adopt(id):
    pet = Pet.query.get_or_404(id)
    pet.available = False
    db.session.commit()
    return redirect(f"/{id}")

@app.route('/<int:id>/delete', methods=["GET"])
def delete(id):
    Pet.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect("/homepage")

@app.route('/<int:id>/edit', methods=["GET", "POST"])
def edit_pet(id):
    pet_data = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet_data)
    if form.validate_on_submit():
        pet = Pet()
        pet.edit_pet(id, form)
        return redirect("/homepage")
    else:
        return render_template('/edit.html', form=form, pet=pet_data)
