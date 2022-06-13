def adicionar(lista, produto):
    lista.append(produto)

def exibir(lista):
    lista.sort()
    listaemtexto = ''.join([str(num) for num in lista])
    print(listaemtexto)

def remover(lista, produto):
    for nome in lista:
        if(nome == produto):
            lista.remove(produto)
            return
    print(f'código {produto} não encontrado')
def encerrar(lista):
    exibir(lista)
carrinho = list(map(int, input().split()))
while(True):
    comando = list(map(str, input().split()))
    if comando[0] == 'adicionar':
        adicionar (carrinho, int(comando[1]))
    
    elif comando[0] == 'exibir':
        exibir (carrinho)
    elif comando[0] == 'remover':
        remover(carrinho, int(comando[1]))
    elif comando[0] == 'encerrar':
        encerrar(carrinho)
        break