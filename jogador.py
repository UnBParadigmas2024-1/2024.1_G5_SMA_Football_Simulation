
import random
from mesa import Agent
from bola import Bola

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

    def direction(self, player_type):
        # agents_position = FutebolModel.get_agent_positions()
        direction = ['up', 'down']
        if player_type == "Jogador_T1_atacante" or player_type == "Jogador_T2_atacante" or player_type == "Jogador_T1_goleiro" or player_type == "Jogador_T2_goleiro" or player_type == "Jogador_T1_zagueiro" or player_type == "Jogador_T2_zagueiro":
            if Bola.posicao[0] >= self.pos[0]:
                if Bola.posicao[1] >= self.pos[1]:
                    direction = ['up', 'right']
                else:
                    direction = ['down', 'right']
            elif Bola.posicao[0] < self.pos[0]:
                if Bola.posicao[0] < self.pos[0]:
                    direction = ['down', 'left']
                else:
                    direction = ['up', 'left']

        # elif player_type == "Jogador_T1_meia":
        #     x = 0
        #     y = 0
        #     for pos in agents_position["Jogador_T2_atacante"]:
        #         x_2, y_2 = pos
        #         x += x_2
        #         y += y_2

        #     if x >= self.pos[0]:
        #         if y >= self.pos[1]:
        #             direction = ['up', 'right']
        #         else:
        #             direction = ['down', 'right']

        #     if x < self.pos[0]:
        #         if y < self.pos[1]:
        #             direction = ['down', 'left']
        #         else:
        #             direction = ['up', 'left']

        # elif player_type == "Jogador_T2_meia":
        #     x = 0
        #     y = 0
        #     for pos in agents_position["Jogador_T1_atacante"]:
        #         x_2, y_2 = pos
        #         x += x_2
        #         y += y_2

        #     if x >= self.pos[0]:
        #         if y >= self.pos[1]:
        #             direction = ['up', 'right']
        #         else:
        #             direction = ['down', 'right']

        #     if x < self.pos[0]:
        #         if y < self.pos[1]:
        #             direction = ['down', 'left']
        #         else:
        #             direction = ['up', 'left']

        return direction

    def move(self, allowed_y_min, allowed_y_max, direction):   
        x, y = self.pos
        direction_sel = direction[random.randint(0, 1)]

        if direction_sel == 'up':
            new_x, new_y = x, y + 5
        elif direction_sel == 'down':
            new_x, new_y = x, y - 5
        elif direction_sel == 'left':
            new_x, new_y = x - 5, y
        elif direction_sel == 'right':
            new_x, new_y = x + 5, y

        # Checa se a nova posição está dentro da área permitida
        if (0 <= new_x < self.model.grid.width and 
            allowed_y_min <= new_y < allowed_y_max and
            self.energia > 0):
            self.model.grid.move_agent(self, (new_x, new_y))
            self.pos = (new_x, new_y)
            print(f"{self.nome} está correndo. Energia restante: {self.energia}")
            self.energia -= self.random.randint(1, 3)
        # Regenera energia caso não se mova e energia estiver abaixo de 90
        elif (self.energia < 90):
            print(f"{self.nome} está parado. Energia restante: {self.energia}")
            self.energia += self.random.randint(1, 3)

class T1_Goleiro(Jogador):
    # Só se movimenta na área em frente ao gol
    def move(self):
        super().move(0, self.model.grid.height // 15, self.direction("Jogador_T1_goleiro"))
        #print("teste")

class T1_Zagueiro(Jogador):
    # Só se movimenta na metade superior do campo
    def move(self):
        super().move(0, self.model.grid.height // 2, self.direction("Jogador_T1_zagueiro"))

class T1_Meia(Jogador):
    # Só se movimenta na metade central do campo
    def move(self):
        super().move(self.model.grid.height // 4, 3 * self.model.grid.height // 4, self.direction("Jogador_T1_meia"))
class T1_Atacante(Jogador):
    # Só se movimenta na metade inferior do campo
    def move(self):
        super().move(self.model.grid.height // 2, self.model.grid.height, self.direction("Jogador_T1_atacante"))

class T2_Goleiro(Jogador):
    ## Só se movimenta na área em frente ao gol
    def move(self):
        super().move(14 * self.model.grid.height // 15, self.model.grid.height, self.direction("Jogador_T2_goleiro"))

class T2_Zagueiro(Jogador):
    # Só se movimenta na metade inferior do campo
    def move(self):
        super().move(self.model.grid.height // 2, self.model.grid.height, self.direction("Jogador_T2_zagueiro"))

class T2_Meia(Jogador):
    # Só se movimenta na metade central do campo
    def move(self):
        super().move(self.model.grid.height // 4, 3 * self.model.grid.height // 4, self.direction("Jogador_T2_meia"))

class T2_Atacante(Jogador):
    # Só se movimenta na metade superior do campo
    def move(self):
        super().move(0, self.model.grid.height // 2, self.direction("Jogador_T2_atacante"))
        