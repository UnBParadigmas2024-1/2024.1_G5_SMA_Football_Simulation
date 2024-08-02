from mesa import Agent

class Bola(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.posicao = (0, 0)

    def step(self):
        pass 
