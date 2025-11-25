from . import api
from swagger.namespaces.cake_namespace import cakes_ns
from swagger.namespaces.customer_namespace import customers_ns

# Função para registrar os namespaces
def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(cakes_ns, path="/cakes")
    api.add_namespace(customers_ns, path="/")
    api.mask_swagger = False