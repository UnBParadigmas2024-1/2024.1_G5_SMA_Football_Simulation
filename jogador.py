
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
            self.move()

    def acao(self):
        if not self.model.running:  
            return 
        
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

        print(f"{self.nome} está correndo. Energia restante: {self.energia}")
        self.energia -= self.random.randint(1, 3)

    def move(self, allowed_y_min, allowed_y_max):
        if not self.model.running:  
            print(f"{self.nome} está parado. Energia restante: {self.energia}")
            self.energia += self.random.randint(1, 3)
            return 
        
        x, y = self.pos
        direction = self.random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up':
            new_x, new_y = x, y + 5
        elif direction == 'down':
            new_x, new_y = x, y - 5
        elif direction == 'left':
            new_x, new_y = x - 5, y
        elif direction == 'right':
            new_x, new_y = x + 5, y

        # Checa se a nova posição está dentro da área permitida
        if (0 <= new_x < self.model.grid.width and 
            allowed_y_min <= new_y < allowed_y_max and
            self.energia > 0):
            self.model.grid.move_agent(self, (new_x, new_y))
            self.pos = (new_x, new_y)
            print(f"{self.nome} está correndo. Energia restante: {self.energia}")
            self.energia -= self.random.randint(1, 3)
        # Regenera energia caso não se mova
        elif (self.energia < 90):
            print(f"{self.nome} está parado. Energia restante: {self.energia}")
            self.energia += self.random.randint(1, 3)

class T1_Zagueiro(Jogador):
    # Só se movimenta na metade superior do campo
    def move(self):
        super().move(0, self.model.grid.height // 2)

class T1_Meia(Jogador):
    # Só se movimenta na metade central do campo
    def move(self):
        super().move(self.model.grid.height // 4, 3 * self.model.grid.height // 4)

class T1_Atacante(Jogador):
    # Só se movimenta na metade inferior do campo
    def move(self):
        super().move(self.model.grid.height // 2, self.model.grid.height)

class T2_Zagueiro(Jogador):
    # Só se movimenta na metade inferior do campo
    def move(self):
        super().move(self.model.grid.height // 2, self.model.grid.height)

class T2_Meia(Jogador):
    # Só se movimenta na metade central do campo
    def move(self):
        super().move(self.model.grid.height // 4, 3 * self.model.grid.height // 4)

class T2_Atacante(Jogador):
    # Só se movimenta na metade superior do campo
    def move(self):
        super().move(0, self.model.grid.height // 2)