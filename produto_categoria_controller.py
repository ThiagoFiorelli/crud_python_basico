from Produto import Produto
from Categoria import Categoria
from Produto_Categoria import Produto_Categoria
from categoria_controller import get_categoria_by_id

lista_produtos_categorias = []

def cadastro_produto_categoria(lista_categorias : list, produto_id : int, edicao = False):
    lista_ids = []

    # if edicao:
    #     lista_remover = [e for e in lista_produtos_categorias if e.id_produto == produto_id]
    #     lista_produtos_categorias = set(lista_produtos_categorias).difference(lista_remover)

    if not lista_categorias:
        print('Ainda nao existe nenhuma categoria cadastrada.')
    else:
        for c in lista_categorias:
                lista_ids.append(c.get_id())
                print('id: ' + str(c.get_id()) +'| Nome: ' + c.get_nome())
        try:
            op = int(input('Selecione a categoria que deseja adicionar pelo id: '))
            if op in lista_ids:
                produto_categoria = Produto_Categoria(produto_id, op)
                lista_produtos_categorias.append(produto_categoria)
                print('Categoria adicionada.')
            else:
                print('Categoria não encontrada.')
        except ValueError:
            print('O id precisa ser um numero inteiro.')

def listar_produto_categorias(produto_id : int) -> list:
    retorno = []
    for pc in lista_produtos_categorias:
        if pc.id_produto == produto_id:
            retorno.append(get_categoria_by_id(pc.id_categoria).get_nome())
    return retorno

def remover_produto_categoria(produto_id : int):
    for pc in lista_produtos_categorias:
        if pc.id_produto == produto_id:
            lista_produtos_categorias.remove(pc)