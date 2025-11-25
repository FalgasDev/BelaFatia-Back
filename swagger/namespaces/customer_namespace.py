from flask_restx import Namespace, Resource, fields
from models.costumer_model import register, login

customers_ns = Namespace("customers", description="Operações relacionadas aos clientes")

register_model = customers_ns.model("RegisterInput", {
    "name": fields.String(required=True, description="Nome do cliente"),
    "email": fields.String(required=True, description="Email do cliente"),
    "password": fields.String(required=True, description="Senha do cliente")
})

login_model = customers_ns.model("LoginInput", {
    "email": fields.String(required=True, description="Email do cliente"),
    "password": fields.String(required=True, description="Senha do cliente")
})

@customers_ns.route("register")
class RegisterResource(Resource):
    @customers_ns.expect(register_model)
    def post(self):
        """Cria um novo cliente"""
        data = customers_ns.payload
        register(data)
        return {'message': 'Cliente cadastrado com sucesso.'}, 201

@customers_ns.route("login")
class LoginResource(Resource):
    @customers_ns.expect(login_model)
    def post(self):
        """Faz o login"""
        data = customers_ns.payload
        login(data)
        return {'message': 'Login feito com sucesso.'}, 200