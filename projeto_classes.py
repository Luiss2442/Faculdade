class Viagem: #SUPER CLASSE.
    def __init__(self, contratante, placa, destino, saida, retorno, preco):
        self.placa = placa
        self.contratante = contratante
        self.destino = destino
        self.saida = saida 
        self.retorno = retorno
        self.preco = preco

    def __str__(self): #str representação string de objeto.
        return f"Nome do contratante: {self.contratante}, Placa:  {self.placa}, Destino: {self.destino}, Saida: {self.saida}, Retorno: {self.retorno}, Preco: {self.preco}"

def adicionar_viagem(lista_viagens): #função adicionar viagem.
    contratante = input("Nome do contratante: ")
    placa = input("Placa do veiculo: ")
    destino = input("Digite o destino da viagem: ")
    saida = input("Data de saida: ")
    retorno = input("Data de retorno: ")
    preco = float(input("Digite o preço da viagem: "))
    
    
    nova_viagem = Viagem(contratante, placa, destino, saida, retorno, preco) # Objeto baseado na classe mãe.
    lista_viagens.append(nova_viagem) #adicionar elementos numa lista.
    print("Viagem adicionada.")

def excluir_viagem(lista_viagens): #função excluir viagem.
    if not lista_viagens:
        print("Não há viagens para deletar.")
        return
    
    for idx, viagem in enumerate(lista_viagens): # idx = indice do elemento começando em 0, enumerate para enumerar os itens da lista.
        print(f"{idx + 1} - {viagem}")
    
    indice = int(input("Digite o número da viagem para deletar: ")) -1 #-1 pois a contagem começa em 0.
    
    if 0 <= indice < len(lista_viagens): #len é usado para para o numero de itens numa lista, 
        excluida = lista_viagens.pop(indice) # .pop remove elemento em x posição e retorna para a variavel excluida.
        print(f"Viagem para {excluida.destino} deletada.")
    else:
        print("Não existe essa viagem.")

def ver_viagens(lista_viagens): #ver viagens.
    if not lista_viagens:
        print("Nenhuma viagem adicionada.")
        return
    
    print("Viagens adicionadas:")
    for viagem in lista_viagens:
        print(viagem)

def menu(): #menu propriamente dito.
    lista_viagens = []
    while True:
        print("\n Opções:")
        print("1 - Adicionar viagem")
        print("2 - Deletar viagem")
        print("3 - Ver viagens")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_viagem(lista_viagens)
        elif opcao == "2":
            excluir_viagem(lista_viagens)
        elif opcao == "3":
            ver_viagens(lista_viagens)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inexistente. Tente novamente.")


menu()
