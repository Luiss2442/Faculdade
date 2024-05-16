class Computador:
    def __init__(self, ram, cpu, so):
    
        self.ram = ram
        self.cpu = cpu
        self.so = so
    
    def introducao(self):
        print(f'RAM:  {self.ram} CPU {self.cpu} SO: {self.so}')

    def desligar(self):
        print("Estou desligando")

    def ligar(self):
        print("Ligando!")

desk = Computador('16gb', 'AMD Ryzen 7', 'Windows 98')

desk.ligar()
desk.introducao()
desk.desligar()

computador2 = Computador('2gb', 'Duo Core', 'Windos 95')
computador2.ligar()
computador2.introducao()
computador2.desligar()