cardapio = {}

def adicionar_item(nome, preco):

    if nome in cardapio:
        print(f"O Item {nome} já está cadastrado!")
    else:
        cardapio[nome] = preco
        print(f"Item {nome} adicionado com sucesso!")

adicionar_item("Café", 5)


def listar_cardapio():
    if not cardapio:
        print("Cardápio vazio!")
    else :
        print("Itens do Cardápio:")
        for nome, preco in cardapio.items():
            print(f"{nome} - R${preco}")


def atualizar_item(nome, novo_preco):
    if nome in cardapio:
        cardapio[nome] = novo_preco
        print(f"O Item {nome} foi atualizado com sucesso para R${novo_preco}!")
    else:
        print(f"Item {nome} não existe no cardapio!")

atualizar_item("Café", 50)


def remover_item(nome):
    if nome in cardapio:
        del cardapio[nome]
        print(f"Item {nome} removido com sucesso!")
    else:
        print(f"Item {nome} não existe no cardapio!")

remover_item("Café")

print(cardapio)