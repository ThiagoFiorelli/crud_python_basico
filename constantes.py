produto_id = -1
categoria_id = -1

def get_new_id(tipo) -> int:
    if tipo == 'produto':
        global produto_id
        produto_id += 1
        return produto_id

    if tipo == 'categoria':
        global categoria_id
        categoria_id += 1
        return categoria_id
