from Produto import Produto
from produto_categoria_controller import listar_produto_categorias, remover_produto_categoria

lista_produtos = []

def cadastro_produto_tipo(tipo):
    if tipo == 'nome':
        nome = input('Digite o nome do produto: ')
        return nome
    
    elif tipo == 'descricao':
        descricao = input('Digite a descrição do produto (min 20 caracteres): ')
        if len(descricao) < 20:
            print('A descrição precisa ter no mínimo 20 caracteres.')
            return cadastro_produto_tipo('descricao')
        else:
            return descricao

    elif tipo == 'preco':
        try:
            preco = float(input('Digite o preço do produto: '))
            return preco
        except ValueError:
            print('O preço precisa ser um número.')
            return cadastro_produto_tipo('preco')

def cadastrar_produto(produto : Produto = None) -> int:
    existe = True
    if not produto:
        produto = Produto()
        existe = False

    produto.set_nome(cadastro_produto_tipo('nome'))
    produto.set_descricao(cadastro_produto_tipo('descricao'))
    produto.set_preco(cadastro_produto_tipo('preco'))

    if not existe:
        lista_produtos.append(produto)
    
    return produto.get_id()

def listar_produtos():
    if not lista_produtos:
        print('Lista de produtos está vazia!')
    else:
        for p in lista_produtos:
            print('Produto: ')
            print('id: ' + str(p.get_id()) +'| Nome: ' + p.get_nome() + '| Descrição: ' + p.get_descricao() + '| Preço: R$' + str(p.get_preco()))
            print('Categorias do produto: ')
            lista_produto_categorias = listar_produto_categorias(p.get_id())
            if not lista_produto_categorias:
                print('Esse produto não possui categorias. \n')
            else:
                print(str(lista_produto_categorias) + '\n')


def editar_produto(prod : Produto):
    cadastrar_produto(prod)

def remover_produto(prod : Produto):
    lista_produtos.remove(prod)
    remover_produto_categoria(prod.get_id())
    
def get_produto_by_id(id_produto : int) -> Produto:
    for p in lista_produtos:
        if p.get_id() == id_produto:
            return p