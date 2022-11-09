from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    """Pet"""

    __tablename__ = "pets"

    def __repr__(self):
        p = self
        return f"<Pet {p.id}: {p.name} species: {p.species} available: {p.available}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean)

    def submit_pet(self, form):
        name = form.name.data
        species = form.species.data
        photo_url = form.photo.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes, available=available)
        db.session.add(pet)
        return db.session.commit()

    def edit_pet(self, petId, form):
        pet = Pet.query.get(petId)
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        return db.session.commit()



def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
