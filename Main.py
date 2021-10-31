from Pessoa import Pessoa
from Caixa import Caixa
from Produto import Produto


def main():
    pessoa1 = Pessoa()
    pessoa2 = Pessoa()
    pessoa3 = Pessoa()
    pessoa4 = Pessoa()

    caixa1 = Caixa()
    caixa2 = Caixa()
    caixa3 = Caixa()
    caixa4 = Caixa()

    produto1 = Produto()
    produto2 = Produto()
    produto3 = Produto()
    produto4 = Produto()

    pessoa1.set_nome("João")
    pessoa2.set_nome("Maria")
    pessoa3.set_nome("Pedro")
    pessoa4.set_nome("José")

    caixa1.set_nome("Caixa 1")
    caixa2.set_nome("Caixa 2")
    caixa3.set_nome("Caixa 3")
    caixa4.set_nome("Caixa 4")
    
    caixa1.entrar([pessoa1])
    caixa2.entrar([pessoa2])
    caixa3.entrar([pessoa3])
    caixa4.entrar([pessoa4])

    caixa1.abrir()
    caixa2.abrir()
    caixa3.abrir()
    caixa4.abrir()

    print("Quantidade de pessoas no caixa: {}".format(caixa1.__len__()))
    print("Quantidade de pessoas no caixa: {}".format(caixa2.__len__()))
    print("Quantidade de pessoas no caixa: {}".format(caixa3.__len__()))
    print("Quantidade de pessoas no caixa: {}".format(caixa4.__len__()))

    produto1.set_nome("Coca-cola")
    produto2.set_nome("Doritos")
    produto3.set_nome("Nesgresco")
    produto4.set_nome("Kit-Kat")

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
    
    pessoa3.remover_produto("Nesgresco")
    print("O {}, comprou esses itens {} no caixa {} e o total da compra foi de R${}".format(pessoa1.get_nome(), pessoa1.get_compras(), caixa1.get_nome(), pessoa1.total()))
    print("O {}, comprou esses itens {} no caixa {} e o total da compra foi de R${}".format(pessoa2.get_nome(), pessoa2.get_compras(), caixa2.get_nome(), pessoa2.total()))
    print("O {}, comprou esses itens {} no caixa {} e o total da compra foi de R${}".format(pessoa3.get_nome(), pessoa3.get_compras(), caixa3.get_nome(), pessoa3.total()))
    print("O {}, comprou esses itens {} no caixa {} e o total da compra foi de R${}".format(pessoa4.get_nome(), pessoa4.get_compras(), caixa4.get_nome(), pessoa4.total()))

    caixas = [caixa1,caixa2,caixa3,caixa4]
    caixa4.fechar(caixas, caixa4)
    # caixa3.fechar(caixas, caixa3)
    # caixa2.fechar(caixas, caixa2)
    p = caixa1.fechar(caixas, caixa1)
    print(p)

if __name__ == "__main__":
    main()