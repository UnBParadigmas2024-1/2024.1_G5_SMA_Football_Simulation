
import random
from mesa import Agent

class Jogador(Agent):
    def __init__(self, unique_id, model, nome, team):
        super().__init__(unique_id, model)
        self.nome = nome
        self.team = team
        self.energia = 100
    
    def step(self):
        if self.model.jogo_comecou and self.model.running:  
            self.acao()

    def acao(self):
        if not self.model.running:  
            return 
        
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

        print(f"{self.nome} está correndo. Energia restante: {self.energia}")
        self.energia -= self.random.randint(1, 3)
