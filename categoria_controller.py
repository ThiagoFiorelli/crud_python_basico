from Categoria import Categoria

lista_categorias = [Categoria(-1, 'Eletronicos'), Categoria(-1, 'Alimentos'), Categoria(-1, 'Roupas')]

lista_categorias_pai = lista_categorias.copy()

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

 
    op_cad_subcategoria = input('Deseja atrelar a uma categoria? S/N: ').lower()
    if op_cad_subcategoria == 's':
        categoria.set_pai_id(cadastro_categoria_subcategoria(categoria.get_id()))
    elif op_cad_subcategoria == 'n':
        categoria.set_pai_id(-1)
        lista_categorias_pai.append(categoria)

    if not existe:
        lista_categorias.append(categoria)
    
    return categoria.get_id()

def listar_categorias():
    if not lista_categorias:
        print('Lista de categorias está vazia!')
    else:
        for c in lista_categorias:
            print('Categoria: ')
            print('id: ' + str(c.get_id()) +'| Nome: ' + c.get_nome() +'| Pai: ' + str(c.get_pai_id()))

def editar_categoria(cat):
    cadastrar_categoria(cat)

def remover_categoria(cat):
    if cat.get_pai_id == -1:
        remover_categoria_subcategorias(cat.get_id)
        lista_categorias_pai.remove(cat)
    
    lista_categorias.remove(cat)
    
def get_categoria_by_id(id_categoria) -> Categoria:
    for c in lista_categorias:
        if c.get_id() == id_categoria:
            return c

def cadastro_categoria_subcategoria(categoria_id : int):
    lista_ids = []
    if not lista_categorias_pai:
        print('Ainda nao existe nenhuma categoria pai cadastrada.')
    else:
        for c in lista_categorias_pai:
                lista_ids.append(c.get_id())
                print('id: ' + str(c.get_id()) +'| Nome: ' + c.get_nome() +'| Pai: ' + str(c.get_pai_id()))
        while True:
            try:
                op = int(input('Selecione a categoria pai pelo id: '))
                if op in lista_ids:
                    print('Categoria atrelada a categoria pai.')
                    return op
                else:
                    print('Categoria não encontrada.')
            except ValueError:
                print('O id precisa ser um numero inteiro.')

def remover_categoria_subcategorias(categoria_id : int):
    for cs in lista_categorias:
        if cs.get_pai_id == categoria_id:
            lista_categorias.remove(cs)