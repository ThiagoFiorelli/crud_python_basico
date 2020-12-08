from Categoria import Categoria
from categoria_subcategoria_controller import listar_categoria_subcategorias

lista_categorias = []

def cadastro_categoria_tipo(tipo):
    if tipo == 'nome':
        nome = input('Digite o nome da categoria: ')
        return nome

def cadastrar_categoria(categoria : Categoria = None):
    existe = True
    if not categoria:
        categoria = Categoria()
        existe = False

    categoria.set_nome(cadastro_categoria_tipo('nome'))

    if not existe:
        lista_categorias.append(categoria)
    
    return categoria.get_id()

def listar_categorias():
    if not lista_categorias:
        print('Lista de categorias está vazia!')
    else:
        for c in lista_categorias:
            print('Categoria: ')
            print('id: ' + str(c.get_id()) +'| Nome: ' + c.get_nome())
            print('Subcategorias da categoria: ')
            lista_categoria_subcategorias = listar_categoria_subcategorias(c.get_id())
            if not lista_categoria_subcategorias:
                print('Esse categoria nao possui subacategorias. \n')
            else:
                print(str(lista_categoria_subcategorias) + '\n')

def editar_categoria(cat):
    cadastrar_categoria(cat)

def remover_categoria(cat):
    lista_categorias.remove(cat)
    
def get_categoria_by_id(id_categoria) -> Categoria:
    for c in lista_categorias:
        if c.get_id() == id_categoria:
            return c