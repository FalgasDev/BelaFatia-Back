from config.database import db
from errors import EmptyStringError, AuthError


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
    
def register(data):
    required_fields = ['name', 'email', 'password']
    if not all(field in data for field in required_fields):
        raise KeyError("Algum campo está faltando.")
    
    if not data['name'] or not data['email'] or not data['password']:
        raise EmptyStringError('Todos os campos tem que estar preenchidos.')
    
    customer = Customer.query.filter_by(name=data['email']).first()

    if customer:
        raise AuthError('Cliente já cadastrado com este email.')
    
    new_customer = Customer(
        name=data['name'],
        email=data['email'],
        password=data['password']
    )

    db.session.add(new_customer)
    db.session.commit()

def login(data):
    required_fields = ['email', 'password']
    if not all(field in data for field in required_fields):
        raise KeyError("Algum campo está faltando.")
    
    if not data['email'] or not data['password']:
        raise EmptyStringError('Todos os campos tem que estar preenchidos.')
    
    customer = Customer.query.filter_by(email=data['email']).first()

    if not customer:
        raise AuthError('Email or password are incorrect')
    
    if customer.password != data['password']:
        raise AuthError('Email or password are incorrect')

    return customer.name