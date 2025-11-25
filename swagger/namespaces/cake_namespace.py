from flask_restx import Namespace, Resource, fields
from models.cake_model import getCakes, registerCake, getCakeById, updateCake, deleteCake

cakes_ns = Namespace("cakes", description="Operações relacionadas aos bolos")

cake_model = cakes_ns.model("CakeInput", {
    "name": fields.String(required=True, description="Nome do bolo"),
    "price": fields.String(required=True, description="Preço do bolo"),
    "img": fields.String(required=True, description="Imagem do bolo")
})

cake_output_model = cakes_ns.model("CakeOutput", {
    "id": fields.Integer(description="ID do bolo"),
    "name": fields.String(description="Nome do bolo"),
    "price": fields.String(description="Preço do bolo"),
    "img": fields.String(description="Imagem do bolo")
})

@cakes_ns.route("/")
class CakesResource(Resource):
    @cakes_ns.marshal_list_with(cake_output_model)
    def get(self):
        """Lista todos os bolos"""
        return getCakes()

    @cakes_ns.expect(cake_model)
    def post(self):
        """Cria um novo bolo"""
        data = cakes_ns.payload
        registerCake(data)
        return {'message': 'Bolo cadastrado com sucesso.'}, 201

@cakes_ns.route("/<int:id_cake>")
class CakeIdResource(Resource):
    @cakes_ns.marshal_with(cake_output_model)
    def get(self, id_cake):
        """Obtém um bolo pelo ID"""
        return getCakeById(id_cake)

    @cakes_ns.expect(cake_model)
    def put(self, id_cake):
        """Atualiza um bolo pelo ID"""
        data = cakes_ns.payload
        updateCake(id_cake, data)
        return data, 200

    def delete(self, id_cake):
        """Exclui um aluno pelo ID"""
        deleteCake(id_cake)
        return {"message": "Bolo excluído com sucesso"}, 200