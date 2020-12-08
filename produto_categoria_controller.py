from Produto import Produto
from Categoria import Categoria
from Produto_Categoria import Produto_Categoria
from categoria_controller import get_categoria_by_id

lista_produtos_categorias = []

def cadastro_produto_categoria(lista_categorias, produto_id) -> list:
    lista_ids = []
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

def listar_produto_categorias(produto_id):
    retorno = []
    for pc in lista_produtos_categorias:
        if pc.id_produto == produto_id:
            retorno.append(get_categoria_by_id(pc.id_categoria).get_nome())
    
    return retorno