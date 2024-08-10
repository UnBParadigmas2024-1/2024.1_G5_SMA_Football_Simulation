from mesa import Agent

class Bola(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.posicao = (0, 0)

    def mover(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        print(f"A bola se moveu para {new_position}.")
