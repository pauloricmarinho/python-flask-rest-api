from flask import Flask, request
from flask_restful import Resource, Api
import json
from mock_fabricantes import Fabricante

# Inicializar o Flask
app = Flask(__name__)
api = Api(app)

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

# Recuperar um Produto por ID, também usando para Remover ou Alterar um Produto
class Produto(Resource):
    def get(self, id):
        try:
            response = produtos[id]
        except IndexError:
            mensagem = 'Produto de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        produtos[id] = dados
        return dados

    def delete(self, id):
        produtos.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro Excluído com Sucesso'}

# Lista os Produtos Cadastrados e Permite a Inclusão de Novos Produtos
class ListaProdutos(Resource):
    def get(self):
        return produtos

    def post(self):
        dados = json.loads(request.data)
        posicao = len(produtos)
        dados['id'] = posicao
        produtos.append(dados)
        return produtos[posicao]

api.add_resource(Produto, '/produto/<int:id>')
api.add_resource(ListaProdutos, '/produto')
api.add_resource(Fabricante, '/fabricante/')

if __name__ == '__main__':
    app.run(debug=True)