class Carro:
    def __init__(self, motor, cor, marca):
    
        self.motor = motor
        self.cor = cor
        self.marca = marca
    
    def introducao(self):
        print(f'MOTOR: {self.motor}; COR: {self.cor}; MARCA: {self.marca}')

    def som(self):
        print("Som Ligando!")

    def desligar(self):
        print("Carro desligado!")

    def ligar(self):
        print("Carro ligando!")

civic = Carro('2.0', 'PRETA', 'HONDA')

civic.ligar()
civic.som()
civic.introducao()
civic.desligar()

unomille = Carro('1.0', 'VERMELHO', 'FIAT')

unomille.ligar()
unomille.som()
unomille.introducao()
unomille.desligar()