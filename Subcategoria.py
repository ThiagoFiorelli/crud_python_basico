class Subcategoria:
    __id : int
    __nome : str

    def __init__(self, id):
        self.__id = id

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome
    
    def set_nome(self, nome) -> str:
        if type(nome) == str:
            self.__nome = nome