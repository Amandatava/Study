carrinho = list(map(int, input().split()))
while(True):
    comando = list(map(str, input().split()))
    if comando[0] == 'adicionar':
        adicionar(carrinho, int(comando[1]))
    
    elif comando[0] == 'exibir':
        exibir(carrinho)
    elif comando[0] == 'remover':
        remover(carrinho, int(comando[1]))
    elif comando[0] == 'encerrar':
        encerrar(carrinho)
        break