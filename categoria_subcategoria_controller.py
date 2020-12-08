from Subcategoria import Subcategoria
from Categoria import Categoria
from Categoria_Subcategoria import Categoria_Subcategoria

lista_categoria_subcategorias = []
lista_subcategorias = [Subcategoria(0,'Doces'), Subcategoria(1,'Salgados'), Subcategoria(2,'Periféricos'), Subcategoria(3,'Smartphones'), Subcategoria(4,'PC')]

def cadastro_categoria_subcategoria(categoria_id : int):
    lista_ids = []
    if not lista_subcategorias:
        print('Ainda nao existe nenhuma subcategoria cadastrada.')
    else:
        for c in lista_subcategorias:
                lista_ids.append(c.get_id())
                print('id: ' + str(c.get_id()) +'| Nome: ' + c.get_nome())
        try:
            op = int(input('Selecione a subcategoria que deseja adicionar pelo id: '))
            if op in lista_ids:
                categoria_subcategoria = Categoria_Subcategoria(categoria_id, op)
                lista_categoria_subcategorias.append(categoria_subcategoria)
                print('Subcategoria adicionada.')
            else:
                print('Subcategoria não encontrada.')
        except ValueError:
            print('O id precisa ser um numero inteiro.')

def listar_categoria_subcategorias(categoria_id : int) -> list:
    retorno = []
    for cs in lista_categoria_subcategorias:
        if cs.id_categoria == categoria_id:
            retorno.append(get_subcategoria_by_id(cs.id_subcategoria).get_nome())
    return retorno

def get_subcategoria_by_id(id_categoria) -> Categoria:
    for c in lista_subcategorias:
        if c.get_id() == id_categoria:
            return c

def remover_categoria_subcategorias(categoria_id : int):
    for cs in lista_categoria_subcategorias:
        if cs.id_categoria == categoria_id:
            lista_categoria_subcategorias.remove(cs)