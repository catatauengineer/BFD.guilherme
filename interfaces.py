from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado no cartão de crédito.")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Boleto de R$ {valor:.2f} gerado para pagamento.")

p1 = CartaoCredito()
p2 = Boleto()
p1.processar(150)
p2.processar(200)


class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Computador ligado.")

    def desligar(self):
        print("Computador desligado.")

pc = Computador()
pc.ligar()
pc.desligar()


class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("Relatório impresso.")

    def exportar(self):
        print("Relatório exportado em PDF.")

r = Relatorio()
r.imprimir()
r.exportar()


class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def __init__(self):
        self.dados = {}

    def salvar(self, objeto):
        self.dados[objeto["id"]] = objeto

    def buscar(self, id):
        return self.dados.get(id)

repo = RepositorioMemoria()
repo.salvar({"id": 1, "nome": "Produto A"})
print(repo.buscar(1))
