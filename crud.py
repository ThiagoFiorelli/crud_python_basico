class Produto:
    __id : int
    __nome : str
    __descricao : str
    __preco : int

    def __init__(self):
        self.__id = id_numerador

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome
    
    def set_nome(self, nome) -> str:
        if type(nome) == str:
            self.__nome = nome

    def get_descricao(self) -> str:
        return self.__descricao
    
    def set_descricao(self, descricao) -> str:
        if type(descricao) == str:
            self.__descricao = descricao

    def get_preco(self) -> int:
        return self.__preco
    
    def set_preco(self, preco) -> int:
        if type(preco) == int:
            self.__preco = preco

def cadastro(tipo) -> str:
    if tipo == 'nome':
        nome = input('Digite o nome do produto: ')
        return nome
    
    elif tipo == 'descricao':
        descricao = input('Digite a descrição do produto: ')
        return descricao

    elif tipo == 'preco':
        try:
            preco = int(input('Digite o preço do produto: '))
            return preco
        except ValueError:
            print('O preço precisa ser um inteiro.')
            return cadastro('preco')

def editar(prod) -> Produto:
    prod.set_nome(cadastro('nome'))
    prod.set_descricao(cadastro('descricao'))
    prod.set_preco(cadastro('preco'))

def remover(prod) -> Produto:
    lista_produtos.remove(prod)
    
def get_produto_by_id(id_produto) -> int:
    for p in lista_produtos:
        if p.get_id() == id_produto:
            return p
        

lista_produtos = []
id_numerador = 0
print('Cadastro de Produto.')
while True:
    op = input('C - Cadastrar produto / L - Listar produto / E - Editar produto / R - Remover produto / S - Sair: ').lower()
    if op == 'c':
        produto = Produto()
        produto.set_nome(cadastro('nome'))
        produto.set_descricao(cadastro('descricao'))
        produto.set_preco(cadastro('preco'))
        lista_produtos.append(produto)
        id_numerador += 1
    elif op == 'l':
        for p in lista_produtos:
            print('id: ' + str(p.get_id()) +'| Nome: ' + p.get_nome() + '| Descrição: ' + p.get_descricao() + '| Preço: R$' + str(p.get_preco()))
    elif op == 'e':
        try:
            id_produto_edicao = int(input('Digite o id do produto que deseja editar: '))
            produto = get_produto_by_id(id_produto_edicao)
            if isinstance(produto,Produto):
                editar(produto)
            else:
                print('Produto não encontrado.')
        except ValueError:
            print('O id precisa ser um numero inteiro.')     
    elif op == 'r':
        try:
            id_produto_edicao = int(input('Digite o id do produto que deseja remover: '))
            produto = get_produto_by_id(id_produto_edicao)
            if isinstance(produto,Produto):
                remover(produto)
            else:
                print('Produto não encontrado.')
        except ValueError:
            print('O id precisa ser um numero inteiro.')
    elif op == 's':
        break



