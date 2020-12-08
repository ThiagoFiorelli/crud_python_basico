from constantes import produto_id, get_new_id

class Categoria:
    __id : int
    __nome : str
    __pai_id : int

    def __init__(self, pai_id = -1, nome = None):
        self.__id = get_new_id('categoria')
        self.__pai_id = pai_id
        self.__nome = nome

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome
    
    def set_nome(self, nome : str):
        if type(nome) == str:
            self.__nome = nome
    
    def get_pai_id(self) -> int:
        return self.__pai_id

    def set_pai_id(self, pai_id : int):
        self.__pai_id = pai_id