import os.path

def criarArq(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")

criaArquivo("categoria.txt", "clientes.txt", "estoque.txt", "fornecedor.txt", "funcionario.txt", "venda.txt")


if __name__ == '__main__':
    while True:
        escolha = int(input("\nDigite 1 para acessar (Categorias)\n"
                    "Digite 2 para acessar ( Estoque )\n"
                    "Digite 3 para acessar ( Fornecedor )\n"
                    "Digite 4 para acessar ( Cliente )\n"
                    "Digite 5 para acessar ( Funcionários)\n"
                    "Digite 6 para acessar ( Vendas)\n"
                    "Digite 0 para sair\n"))
        if escolha == 0:
            break
        if escolha == 1:
            while True:
                opcao = int(input("\nDigite 1 para cadastrar uma categoria\n"
                                  "Digite 2 para remover uma categoria\n"
                                  "Digite 3 para alterar uma categoria\n"
                                  "Digite 4 para ver as categorias cadastradads\n"
                                  "Digite 0 para sair"))
                if opcao == 0:
                    break


