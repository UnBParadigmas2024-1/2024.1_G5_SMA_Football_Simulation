from mesa import Agent

class Tecnico(Agent):
    def __init__(self, unique_id, model, nome):
        super().__init__(unique_id, model)
        self.nome = nome

    def step(self):
        self.definir_estrategia()

    def definir_estrategia(self):
        
        jogadores = [agent for agent in self.model.schedule.agents if isinstance(agent, Jogador)]
        for jogador in jogadores:
            if jogador.energia < 20:
                print(f"{self.nome} substituiu {jogador.nome} devido à baixa energia.")
                
