from flask import Flask, request
from flask_restful import Resource, Api
import json
#from mock_fabricantes import Fabricante
from model import Produto, Fabricante, Usuario
from flask_httpauth import HTTPBasicAuth

# Inicializar o Flask
app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

produtos = [
    {'id':0,'nome':'Iphone 14 64GB','valor':14999.99,'categoria':['Eletronico','Mobile','Celular'],'fabricante':'Apple'},
    {'id':1,'nome':'Xbox Series S 1TB','valor':2999.99,'categoria':['Games','Console'],'fabricante':'Microsoft'},
    {'id':2,'nome':'Xiaomi Redmi 8 Pro 128GB','valor':1499.99,'categoria':['Eletronico','Celular'],'fabricante':'Xiaomi'},
    {'id':3,'nome':'Xbox Series X 1TB','valor':4999.99,'categoria':['Games','Console'],'fabricante':'Microsoft'},
    {'id':4,'nome':'Kindle 10th Gen Papperwrite','valor':499.99,'categoria':['Eletronico','E-Reader'],'fabricante':'Amazon'},
    {'id':5,'nome':'Echo Dot Alexa','valor':299.99,'categoria':['Eletronico'],'fabricante':'Amazon'},
    {'id':6,'nome':'Microsoft Office 365','valor':399.99,'categoria':['Software'],'fabricante':'Microsoft'},
    {'id':7,'nome':'PS5 4K 1TB','valor':1999.99,'categoria':['Games','Consone'],'fabricante':'Sony'},    
]

#USER_MOCK = {
#     'prmarinho':'1q2w3e4r' 
#}

#@auth.verify_password
#def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     return USER_MOCK.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuario.query.filter_by(login=login, senha=senha).first()

# Recuperar um Produto por ID, também usando para Remover ou Alterar um Produto
class ProdutoService(Resource):
    @auth.login_required
    def get(self, id):
        produto = Produto.query.filter_by(id=id).first()
        try:
            response = {
            'nome':produto.nome,
            'valor':produto.valor,
            'id':produto.id,
            'fabricante':produto.fabricante.nome
            }
        except IndexError:
            mensagem = 'Produto de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Produto nao encontrado...'
            }
        return response

    def put(self, id):
        produto = Produto.query.filter_by(id=id).first()
        dados = request.json
        if 'nome' in dados:
            produto.nome = dados['nome']
        if 'valor' in dados:
            produto.valor = dados['valor']
        produto.save()
        response = {
            'id':produto.id,
            'nome':produto.nome,
            'valor':produto.valor
        }
        return response

    def delete(self, id):
        produto = Produto.query.filter_by(id=id).first()
        mensagem = 'Produto {} excluido com sucesso'.format(produto.nome)
        produto.delete()
        return {'status':'sucesso', 'mensagem':mensagem}

# Lista os Produtos Cadastrados e Permite a Inclusão de Novos Produtos
class ListaProdutosService(Resource):
    def get(self):

        produtos = Produto.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'valor':i.valor} for i in produtos]
        return response
        

    def post(self):
        dados = request.json
        produto = Produto(nome=dados['nome'], valor=dados['valor'], fabricante_id=dados['fabricante_id'])
        produto.save()
        response = {
            'id':produto.id,
            'nome':produto.nome,
            'valor':produto.valor
        }
        return response

api.add_resource(ProdutoService, '/produto/<int:id>')
api.add_resource(ListaProdutosService, '/produto')
#api.add_resource(Fabricante, '/fabricante/')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)