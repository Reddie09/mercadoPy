from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('=========================================================')
    print('======================Bem-Vindo(a)=======================')
    print('=========================PyShop==========================')
    print('=========================================================')

    print('Selecione uma opção abaixo:')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Comprar Produtos')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair')

    opt: int = int(input())

    if opt == 1:
        cad_produto()
    elif opt == 2:
        listar_produtos()
    elif opt == 3:
        comprar_produto()
    elif opt == 4:
        visualizar_carrinho()
    elif opt == 5:
        fechar_pedido()
    elif opt == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida')
        sleep(1)
        menu()

def cad_produto() -> None:
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O Produto {produto.nome} foi cadastrado com sucesso!')
    sleep(1)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de Produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('--------------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(1)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho')
        print('------------------------------------------------------------')
        for produto in produtos:
            print(produto)
            print('------------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())
        produto: Produto = pega_produto_por_cod(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_carrinho: bool = False
                for item in carrinho:
                    q: int = item.get(produto)
                    if q:
                        item[produto] = q + 1
                        print(f'O produto{produto.nome} agora possui {q + 1} no carrinho')
                        tem_carrinho = True
                        sleep(1)
                        menu()
                if not tem_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(1)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado')
                sleep(1)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado')
            sleep(1)
            menu()
    else:
        print('Ainda não existe produtos pra vender.')
    sleep(1)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho:')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho')
        sleep(1)
        menu()
def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('-------------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre')
        carrinho.clear()
        sleep(1)
    else:
        print('Ainda não existem produtos no Carrinho')
    sleep(1)
    menu()

def pega_produto_por_cod(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()