from mesa import Agent

class Bola(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.trajectory = None  # Direction the ball will move
        self.steps_remaining = 0  # Number of steps to move in that direction
    
    def set_trajectory(self, direction, steps):
        self.trajectory = direction
        self.steps_remaining = steps
    
    def mover(self):
        if self.steps_remaining > 0 and self.trajectory:
            new_position = (self.pos[0] + self.trajectory[0], self.pos[1] + self.trajectory[1])
            if self.model.grid.is_cell_empty(new_position):
                self.model.grid.move_agent(self, new_position)
            self.steps_remaining -= 1
            print(f"A bola se moveu para {self.pos} na direção {self.trajectory}. Passos restantes: {self.steps_remaining}")
        else:
            self.trajectory = None  # Stop moving when steps are done
