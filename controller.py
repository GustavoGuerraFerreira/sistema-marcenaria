from dao import *

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("Categoria cadastrada com sucesso")
        else:
                print("A Categoria já existe")

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) == 0:
            print('A categoria que deseja remover, não existe')
        else: 
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print("Categoria removida com sucesso")
        #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

    def alterarCategoria(self,categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada,x ))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x  ))
            else:
                print("A categoria para qual deseja alterar já existe")
                #TODO: ALTERA A CATEGORIA NO ESTOQUE
        else:
            print("A categoria que deseja alterar não existe")
        
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria():
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia!')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produto(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print("Produto Cadastrado com sucesso")
            else:
                print('Produto já existe em estoque')
        else:
            print('Categoria inexistente')

    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
        else:
            print('O produto que deseja remover não existe')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                               i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x= DaoEstoque.ler()
        y= DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.categoria == novaCategoria, y))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produto( novoNome, novoPreco, novaCategoria), novaQuantidade) if (x.produto.nome ==nomeAlterar)else (x), x))
                    print("Produto alterado com sucesso!")
                else:
                    print("Produto já cadastrado")
            else:
                print('O produto que deseja alterar não existe')

            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                               i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
        else:
            print("A categoria informada não existe")

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print("Estoque vazio")
        else:
            for i in estoque:
                print("\n========Produto========")
                print(f"Nome: {i.produto.nome}\n"
                      f"Preço: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}\n")

class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)
                        DaoVenda.salvar(vendido)
            temp.append([Produto(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        arq = open('estoque.txt', 'w')
        arq.write("")

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                  arq.writelines(i[0].nome + "|" + i[0].preco + "|"+ i[0].categoria + "|" + str(i[1]))
                  arq.writelines('\n')

        if existe == False:
            print('O produto não existe')
            return None
        elif not quantidade:
            print("A quantidade vendida não contém em estoque")
            return None
        else:
            print('venda realizada com sucesso')
            return valorCompra
    
    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        ordenado = []
        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x : x['produto'] ==nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x : {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)} 
                                    if(x['produto'] == nome) else(x), produtos))   
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
            
        ordenado = sorted(produtos, key = lambda k: k['quantidade'], reverse= True)
        print('esses são os produtos mais vendidos')
        a = 1
        for i in ordenado:
            print(f"========= Produto [{a}] =========")
            print(f"Produto: {i['produto']}\n"
                f"Quantidade: {i['quantidade']}\n")
            a += 1

a = ControllerVenda()
a.relatorioProdutos()