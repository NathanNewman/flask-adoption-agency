from app import app
from models import db, Pet

db.drop_all()
db.create_all()

Pet.query.delete()

Riley = Pet(
    name='Riley',
    species='dog',
    photo_url='https://www.advantagepetcare.com.au/sites/g/files/adhwdz311/files/styles/paragraph_image/public/beagle-staring-into-camera_2.jpg?itok=usgJm_2H',
    age=3,
    notes='howls when he is lonely',
    available=True
)

Quincy = Pet(
    name='Quincy',
    species='dog',
    photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaA045WoFqH5cm9wWuTXNHkN2zTY5cL_-o2g&usqp=CAU',
    age=1,
    notes='growls at strangers',
    available=True
)

Daisy = Pet(
    name='Daisy',
    species='dog',
    age=1,
    notes='does not like other dogs',
    available=True
)

Lassey = Pet(
    name='Lassey',
    species='dog',
    age=10,
    photo_url='https://www.chekia.com/LasseyMay07_ForSite_WEB.jpg',
    available=False
)

Natasha = Pet(
    name='Natasha',
    species='cat',
    age=8,
    photo_url='https://excitedcats.com/wp-content/uploads/2020/10/Chartreux-Cat.jpg',
    available=True
)

Goldie = Pet(
    name='Goldie',
    species='fish',
    age=1,
    photo_url='https://www.liveaquaria.com/images/categories/large/lg_39507_Fantail_Goldfish_Red.jpg',
    available=True
)

Raphael = Pet(
    name='Raphael',
    species='turtle',
    age='17',
    photo_url='https://bbts1.azureedge.net/images/p/full/2022/08/1eedf7db-80cf-4df9-90c3-b47350823a37.jpg',
    notes='fights crime',
    available=True
)

db.session.add(Riley)
db.session.add(Quincy)
db.session.add(Daisy)
db.session.add(Lassey)
db.session.add(Natasha)
db.session.add(Goldie)
db.session.add(Raphael)

db.session.commit()
