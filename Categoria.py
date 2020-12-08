from constantes import produto_id, get_new_id

class Categoria:
    __id : int
    __nome : str

    def __init__(self):
        self.__id = get_new_id('categoria')

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome
    
    def set_nome(self, nome : str):
        if type(nome) == str:
            self.__nome = nome