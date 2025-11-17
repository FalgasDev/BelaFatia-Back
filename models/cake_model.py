from config.database import db
from errors import EmptyStringError, AuthError, IdNotExist

class Cake(db.Model):
    __tablename__ = 'cakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    img = db.Column(db.String(255), nullable=False)

    def __init__(self, name, price, img):
        self.name = name
        self.price = price
        self.img = img


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'img': self.img
        }
    
def registerCake(data):
    required_fields = ['name', 'img', 'price']
    if not all(field in data for field in required_fields):
        raise KeyError("Algum campo está faltando.")

    if not data['name'] or not data['img'] or not data['price']:
        raise EmptyStringError('Todos os campos tem que estar preenchidos.')

    if Cake.query.filter_by(name=data['name']).first():
        raise AuthError('Bolo já cadastrado com este nome.')

    new_cake = Cake(
        name=data['name'],
        img=data['img'],
        price=data['price']
    )
    db.session.add(new_cake)
    db.session.commit()

def getCakes():
    cakes = Cake.query.all()
    return [cake.to_dict() for cake in cakes]

def getCakeById(id):
    cake = Cake.query.get(id)

    if not cake:
        raise IdNotExist("O bolo não foi encontrado")
    
    return cake.to_dict()

def updateCake(id, data):
    cake = Cake.query.get(id)
    if not cake:
        raise IdNotExist('O bolo não foi encontrado')

    cake.name = data.get('name', cake.name)
    cake.img = data.get('img', cake.img)
    cake.price = data.get('price', cake.price)

    db.session.commit()

def deleteCake(id):
    cake = Cake.query.get(id)
    if not cake:
        raise IdNotExist('O bolo não foi encontrado')

    db.session.delete(cake)
    db.session.commit()