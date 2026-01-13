from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

dog = Cachorro()
cat = Gato()

print(dog.falar())
print(cat.falar())

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

r = Retangulo(5, 3)
print(r.area())
print(r.perimetro())

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        print("O carro está andando")

class CarroCompleto(Transporte):
    def mover(self):
        print("O carro está andando")

    def parar(self):
        print("O carro parou")

c = CarroCompleto()
c.mover()
c.parar()