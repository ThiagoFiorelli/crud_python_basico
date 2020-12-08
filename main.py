from produto_controller import *
from categoria_controller import *
from produto_categoria_controller import *
from Categoria import Categoria
from Subcategoria import Subcategoria
   
id_numerador_categoria = 0
id_numerador_subcategoria = 0

print('Cadastro de Produto.')
while True:
    op_menu_inicial = input('P - Produtos / C - Categorias / S - Sair: ').lower()
    if op_menu_inicial == 'p':
        while True:
            op = input('C - Cadastrar produto / L - Listar produto / E - Editar produto / R - Remover produto / V - Voltar: ').lower()
            if op == 'c':
                produto_id = cadastrar_produto()
                while True:
                    op_cad_categoria = input('Deseja adicionar categorias? S/N: ').lower()
                    if op_cad_categoria == 's':
                        cadastro_produto_categoria(lista_categorias, produto_id)
                    elif op_cad_categoria == 'n':
                        break
            elif op == 'l':
                listar_produtos()
            elif op == 'e':
                try:
                    id_produto_edicao = int(input('Digite o id do produto que deseja editar: '))
                    produto = get_produto_by_id(id_produto_edicao)
                    if isinstance(produto,Produto):
                        editar_produto(produto)
                    else:
                        print('Produto não encontrado.')
                except ValueError:
                    print('O id precisa ser um numero inteiro.')     
            elif op == 'r':
                try:
                    id_produto_edicao = int(input('Digite o id do produto que deseja remover: '))
                    produto = get_produto_by_id(id_produto_edicao)
                    if isinstance(produto,Produto):
                        remover_produto(produto)
                    else:
                        print('Produto não encontrado.')
                except ValueError:
                    print('O id precisa ser um numero inteiro.')
            elif op == 'v':
                break
    elif op_menu_inicial == 'c':
        while True:
            op = input('C - Cadastrar categoria / L - Listar categoria / E - Editar categoria / R - Remover categoria / V - Voltar: ').lower()
            if op == 'c':
                cadastrar_categoria()
            elif op == 'l':
                listar_categorias()
            elif op == 'e':
                try:
                    id_categoria_edicao = int(input('Digite o id do categoria que deseja editar: '))
                    categoria = get_categoria_by_id(id_categoria_edicao)
                    if isinstance(categoria,Categoria):
                        editar_categoria(categoria)
                    else:
                        print('Categoria não encontrado.')
                except ValueError:
                    print('O id precisa ser um numero inteiro.')     
            elif op == 'r':
                try:
                    id_categoria_edicao = int(input('Digite o id do categoria que deseja remover: '))
                    categoria = get_categoria_by_id(id_categoria_edicao)
                    if isinstance(categoria,Categoria):
                        remover_categoria(categoria)
                    else:
                        print('Categoria não encontrado.')
                except ValueError:
                    print('O id precisa ser um numero inteiro.')
            elif op == 'v':
                break
    elif op_menu_inicial == 's':
        break



