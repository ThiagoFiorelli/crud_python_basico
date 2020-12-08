from constantes import produto_id, get_new_id

class Produto:
    __id : int
    __nome : str
    __descricao : str
    __peso : float
    __preco : float
    __dimensao : str

    def __init__(self):
        self.__id = get_new_id('produto')

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome
    
    def set_nome(self, nome : str):
        if type(nome) == str:
            self.__nome = nome

    def get_descricao(self) -> str:
        return self.__descricao
    
    def set_descricao(self, descricao : str):
        if type(descricao) == str:
            self.__descricao = descricao

    def get_preco(self) -> float:
        return self.__preco
    
    def set_preco(self, preco : float):
        if type(preco) == float:
            self.__preco = preco

    def get_peso(self) -> float:
        return self.__preco
    
    def set_peso(self, peso : float):
        if type(peso) == float:
            self.__peso = peso

    def get_dimensao(self) -> str:
        return self.__dimensao
    
    def set_dimensao(self, dimensao : str):
        if type(dimensao) == str:
            self.__dimensao = dimensao
            