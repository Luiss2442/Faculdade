from os import system
from datetime import datetime


class Viagem:
    def __init__(self, placa, nome, saida, retorno):
   
        self.placa = placa
        self.nome = nome
        self.saida = saida
        self.retorno= retorno
   
    def adicionarplaca(self):
       print(f'Adicione a PLACA: {self.placa}')
   
    def nomecontratante(self):
        print(f'Nome do CONTRATANTE: {self.nome}')
   
    def datasaida(self):
        print(f'Digite a data de SAIDA: {self.saida}')
   
    def dataretorno(self):
        print(f'Digite data de RETORNO: {self.retorno}')


#LISTA PARA ARMAZENAR AS VIAGENS
viagens = []


#MENU PRINCIPAL
def menu():
    print('\n Opções:')
    print('1. Adicionar viagem')
    print('2. Remover viagem')
    print('3. Exibir viagens')
    print('4. Sair')


    escolha_menu = str(input('Escolha uma das opções: '))
    if escolha_menu == '1':
        system('cls')
        adicionar_viagem()
    elif escolha_menu == '2':
        system('cls')
        remover_viagem()    
    elif escolha_menu == '3':
        system('cls')
        exibir_viagens()    
    elif escolha_menu == '4':
        return 1  
    else:
        print('Valor digitado invalido!')
        menu()
   
#INSERINDO INFORMAÇÕES DE VIAGEM
def adicionar_viagem():
    print('-=-=-=- ADICIONANDO UMA VIAGEM -=-=-=-')
   
    viagem1 = Viagem
    viagem1.adicionarplaca = input('Placa do veiculo: ')
    viagem1.nomecontratante = input('Nome do contratante: ')
    viagem1.datasaida = input('Data de ida (dd/mm/aaaa): ')
    viagem1.dataretorno = input('Data de retorno (dd/mm/aaaa):')


   
    #onibus = input('Placa do veiculo: ')
    #nome_contratante = input('Nome do contratante: ')
    #data_ida = input('Data de saida (DD/MM/AAAA): ')
    #data_volta = input('Data de retorno (DD/MM/AAAA): ')
    #valor_viagem = input('Valor da viagem: R$')


    #Adicionando viagem a lista de viagens
    #viagens.append({
        #'Placa do veiculo': onibus,
        #'Nome do contratante': nome_contratante,
        #'Data de saida': data_ida,
        #'Data de retorno': data_volta,
        #'Valor da viagem': valor_viagem
    #})
   
    #print('Viagem adicionada com sucesso!')
    #menu()


# REMOVENDO UMA VIAGEM


def remover_viagem():
    print('-=-=-=- REMOVENDO UMA VIAGEM -=-=-=-')
    placa = input('Digite a placa do veiculo da viagem que deseja remover: ')
   
    # Mostra todas as viagens com a placa especificada
    viagens_encontradas = []
    for index, viagem in enumerate(viagens):
        if viagem['Placa do veiculo'] == placa:
            viagens_encontradas.append((viagem, index))
            print(f"{len(viagens_encontradas)}. Placa do veículo: {viagem['Placa do veiculo']}, Nome do contratante: {viagem['Nome do contratante']}")
   
    if viagens_encontradas:
        opcao = int(input('Digite o número da viagem que deseja remover: '))
        if 1 <= opcao <= len(viagens_encontradas):
            viagem_removida, index_remover = viagens_encontradas[opcao - 1]
            viagens.pop(index_remover)
            print('Viagem removida com sucesso!')
        else:
            print('Opção inválida!')
    else:
        print('Nenhuma viagem encontrada com essa placa!')
   
    menu()


# EXIBINDO AS VIAGENS
def exibir_viagens():    
    print('-=-=-=- EXIBINDO AS VIAGENS -=-=-=-')
    mes_desejado = int(input('Digite o número do mês que deseja visualizar: '))
    print(f'Viagens do mês {mes_desejado}:')
    for viagem in viagens:
        data_ida = datetime.strptime(viagem['Data de saida'], '%d/%m/%Y')
        if data_ida.month == mes_desejado:
            print('-' * 30)
            print('Placa do veículo:', viagem['Placa do veiculo'])
            print('Nome do contratante:', viagem['Nome do contratante'])
            print('Data de saída:', viagem['Data de saida'])
            print('Data de retorno:', viagem['Data de retorno'])
            #print('Valor da viagem: R$', viagem['Valor da viagem'])
            print('-' * 30)
    menu()


#CHAMADA PARA O MENU PRINCIPAL
menu()
