import random
from mesa import Agent


class Jogador(Agent):
    def __init__(self, unique_id, model, nome):
        super().__init__(unique_id, model)
        self.nome = nome
        self.energia = 100 
    
    def step(self):
        if self.model.jogo_comecou and self.model.running:  
            self.acao()

    def acao(self):
        if not self.model.running:  
            return 

        print(f"{self.nome} está correndo. Energia restante: {self.energia}")
        self.energia -= random.randint(1, 3) 
