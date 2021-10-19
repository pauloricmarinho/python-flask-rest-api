from flask_restful import Resource

lista_fabricantes = ['Amazon', 'Apple', 'Microsoft', 'Sony','Xiaomi','Logitech']
class Fabricante(Resource):
    def get(self):
        return lista_fabricantes