class Produto_Categoria:
    id_produto : int
    id_categoria : int

    def __init__(self, id_produto : int, id_categoria : int):
        self.id_produto = id_produto
        self.id_categoria = id_categoria