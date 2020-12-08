from Categoria import Categoria

lista_categorias = []

def cadastro_categoria_tipo(tipo):
    if tipo == 'nome':
        nome = input('Digite o nome da categoria: ')
        return nome

def cadastrar_categoria(categoria = None):
    existe = True
    if not categoria:
        categoria = Categoria()
        existe = False

    categoria.set_nome(cadastro_categoria_tipo('nome'))

    if not existe:
        lista_categorias.append(categoria)

def listar_categorias():
    if not lista_categorias:
        print('Lista de categorias está vazia!')
    else:
        for c in lista_categorias:
            print('Categoria: ')
            print('id: ' + str(c.get_id()) +'| Nome: ' + c.get_nome() + '\n')

def editar_categoria(cat):
    cadastrar_categoria(cat)

def remover_categoria(cat):
    lista_categorias.remove(cat)
    
def get_categoria_by_id(id_categoria) -> Categoria:
    for c in lista_categorias:
        if c.get_id() == id_categoria:
            return c