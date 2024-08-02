from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from jogador import Jogador
from bola import Bola
from arbitro import Arbitro

class FutebolModel(Model):
    def __init__(self, duracao_jogo):
        super().__init__()  
        self.grid = MultiGrid(20, 20, True)
        self.schedule = RandomActivation(self)
        self.tempo_decorrido = 0
        self.duracao_jogo = duracao_jogo  
        self.running = True  
        self.jogo_comecou = False 
        
        for i in range(22):
            nome = f"Jogador_{i+1}"
            jogador = Jogador(i, self, nome)
            self.schedule.add(jogador)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(jogador, (x, y))

        bola = Bola(22, self)
        self.schedule.add(bola)
        self.grid.place_agent(bola, (10, 10))
        
        arbitro = Arbitro(23, self, "Árbitro Principal")
        self.schedule.add(arbitro)
        self.grid.place_agent(arbitro, (0, 0))
    
    def step(self):
        self.schedule.step()
        self.tempo_decorrido += 1
        if not self.jogo_comecou and self.tempo_decorrido > 0:
            self.jogo_comecou = True  
        print(f"Tempo decorrido: {self.tempo_decorrido} minuto(s)")
        if self.tempo_decorrido >= self.duracao_jogo:
            self.running = False  
