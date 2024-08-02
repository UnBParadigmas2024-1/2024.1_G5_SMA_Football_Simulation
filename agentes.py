class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
        self.energia = 100
    
    def correr(self):
        if self.energia > 0:
            self.energia -= 1
            print(f"{self.nome} está correndo. Energia restante: {self.energia}")
        else:
            print(f"{self.nome} está cansado e não pode correr.")

    def chutar(self):
        if self.energia > 0:
            self.energia -= 2
            print(f"{self.nome} chutou a bola. Energia restante: {self.energia}")
        else:
            print(f"{self.nome} está cansado e não pode chutar.")

class Bola:
    def __init__(self):
        self.posicao = (0, 0)

    def mover(self, nova_posicao):
        self.posicao = nova_posicao
        print(f"A bola foi movida para {self.posicao}")

class Arbitro:
    def __init__(self, nome):
        self.nome = nome

    def apitar(self):
        print(f"{self.nome} apitou o jogo.")

# Criando os jogadores
jogadores_time1 = [Jogador(f"Jogador1_{i}", f"Posicao_{i}") for i in range(1, 12)]
jogadores_time2 = [Jogador(f"Jogador2_{i}", f"Posicao_{i}") for i in range(1, 12)]

# Criando a bola
bola = Bola()

# Criando o árbitro
arbitro = Arbitro("Árbitro Principal")

# Simulação simples
jogadores_time1[0].correr()
jogadores_time1[0].chutar()
bola.mover((10, 20))
arbitro.apitar()
