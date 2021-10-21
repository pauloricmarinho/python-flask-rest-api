from model import Fabricante, Produto, Usuario
import pytest

@pytest.mark.smoke
def test_send_http():
    assert True
# Insere dados na tabela pessoa
def insere_fabricante():
    fabr = Fabricante(id=2,nome='Google')
    print(fabr)
    fabr.save()

# Consultar dados na tabela Fabricante
def consulta_fabricante():
    fabricantes = Fabricante.query.all()
    print(fabricantes)
    fabr = Fabricante.query.filter_by(id=2).first()
    print(fabr.id,fabr.nome)

# Altera dados na tabela Fabricante
def altera_fabricante():
    fabr = Fabricante.query.filter_by(nome='Google').first()
    fabr.nome = 'Amazon'
    fabr.save()

# Exclui dados na tabela Fabricante
def exclui_fabricante():
    fabr = Fabricante.query.filter_by(nome='Google').first()
    fabr.delete()

# Inserir dados na tabela Produtos
def insere_produto():
    prd = Produto(nome='Google Home', valor=199.99, fabricante_id = 1)
    print(prd)
    prd.save()

# Consultar dados na tabela Produtos
def consulta_produto():
    produtos = Produto.query.all()
    print(produtos)

def insere_usuario(login, senha):
    usuario = Usuario(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuario.query.all()
    print(usuarios)


if __name__ == '__main__':
    #insere_fabricante()
    #altera_fabricante()
    #exclui_fabricante()
    #consulta_fabricante()
    #insere_produto()
    #consulta_produto()
    insere_usuario('prmarinho', '01234')
    consulta_todos_usuarios()
    test_send_http()