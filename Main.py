from Pessoa import Pessoa
from Caixa import Caixa
from Produto import Produto


def main():
    pessoa1 = Pessoa()
    pessoa2 = Pessoa()
    pessoa3 = Pessoa()
    pessoa4 = Pessoa()

    pessoa1.set_nome("João")
    pessoa2.set_nome("Maria")
    pessoa3.set_nome("Pedro")
    pessoa4.set_nome("José")

    print("Nome da pessoa: {}".format(pessoa1.get_nome()))
    print("Nome da pessoa: {}".format(pessoa2.get_nome()))
    print("Nome da pessoa: {}".format(pessoa3.get_nome()))
    print("Nome da pessoa: {}".format(pessoa4.get_nome()))


    caixa1 = Caixa()
    caixa2 = Caixa()
    caixa3 = Caixa()
    caixa4 = Caixa()

    caixa1.set_nome("Caixa 1")
    caixa2.set_nome("Caixa 2")
    caixa3.set_nome("Caixa 3")
    caixa4.set_nome("Caixa 4")
    
    print("Nome do caixa: {}".format(caixa1.get_nome()))
    print("Nome do caixa: {}".format(caixa2.get_nome()))
    print("Nome do caixa: {}".format(caixa3.get_nome()))
    print("Nome do caixa: {}".format(caixa4.get_nome()))
    pessoas = [pessoa1, pessoa2, pessoa3, pessoa4]
    print(len(pessoas))

    caixa1.entrar(pessoas)
    print("Quantidade de pessoas no caixa: {}".format(caixa1.__len__()))

    produto1 = Produto()
    produto2 = Produto()
    produto3 = Produto()
    produto4 = Produto()

    produto1.set_nome("Produto 1")
    produto2.set_nome("Produto 2")
    produto3.set_nome("Produto 3")
    produto4.set_nome("Produto 4")

    produto1.set_preco(10)
    produto2.set_preco(20)
    produto3.set_preco(30)
    produto4.set_preco(40)

    compra1 = [produto1, produto2]
    compra2 = [produto3, produto4]
    compra3 = [produto1, produto2, produto3, produto4]
    compra4 = [produto4]

    pessoa1.compras(compra1)
    pessoa2.compras(compra2)
    pessoa3.compras(compra3)
    pessoa4.compras(compra4)

    print(pessoa1.total())
    print(pessoa2.total())
    print(pessoa3.total())
    print(pessoa4.total())


if __name__ == "__main__":
    main()