class Computador: #SUPERCLASSE PAI
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


class Desktop(Computador): #SUBCLASSE FILHO (entre parenteses SUPERCLASSE "pai")
    def __init__(self, ram, cpu, so, rgb):
        super().__init__(ram, cpu, so)
       
        self.rgb = rgb
       
        print("SUBCLASSE FILHO")    


    def ligar(self):
        print("Sou o DESKTOP da SUBCLASSE e estou ligando!")
        print(f"RGB ligado no periférico: {self.rgb}")


    def introducao2(self):
        print(f'o RGB do {self.rgb} estao piscando')


computador2 = Computador('2gb', 'Duo Core', 'Windows 95',)
computador2.ligar()
computador2.introducao()
computador2.desligar()


computador1 = Desktop('16gb', 'AMD Ryzen 7', 'Windows 98', 'Teclado e Mouse')


computador1.ligar()
computador1.introducao()
computador1.introducao2()
computador1.desligar()
