class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

autor = Pessoa("Machado")
livro = Livro("Dom Casmurro", autor)


class Onibus:
    def transportar(self, nome):
        print(nome, "indo para a escola")

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def ir_para_escola(self, onibus):
        onibus.transportar(self.nome)

onibus = Onibus()
aluno = Aluno("Carlos")
aluno.ir_para_escola(onibus)


class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar(self, funcionario):
        self.funcionarios.append(funcionario)

f1 = Funcionario("Ana")
f2 = Funcionario("Bruno")

dep = Departamento("TI")
dep.adicionar(f1)
dep.adicionar(f2)


class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar(self, jogador):
        self.jogadores.append(jogador)

j1 = Jogador("Neymar", "Atacante")
j2 = Jogador("Casemiro", "Volante")

time = Time("Brasil")
time.adicionar(j1)
time.adicionar(j2)

class Motor:
    pass

class Carro:
    def __init__(self):
        self.motor = Motor()

carro = Carro()
del carro


class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = [
            Comodo("Sala"),
            Comodo("Cozinha"),
            Comodo("Quarto"),
            Comodo("Banheiro")
        ]

casa = Casa()
