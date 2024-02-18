from typing import List, Dict

class Produtos():
    produtos: List[Dict[str, any]] = [
        {
        "id": 1,
        "nome" : "Smartphone",
        "descricao": "Um telefone que inteligente",
        "preco": 1500.0
        },
        {
        "id": 2,
        "nome" : "Notebook",
        "descricao": "Um computador movel",
        "preco": 3500.0
        },
        {
        "id": 3,
        "nome" : "Tablet",
        "descricao": "Um computador movel",
        "preco": 2500.0
        },
    ]

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto.get("id") == id:
                return produto
        return {"Status": 401, "Mensagem":"Produto nao encontrado"}
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto.dict())
        return produto