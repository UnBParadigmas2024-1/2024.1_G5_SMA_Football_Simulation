from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from jogador import Jogador, T1_Goleiro, T1_Zagueiro, T1_Meia, T1_Atacante, T2_Goleiro, T2_Zagueiro, T2_Meia, T2_Atacante
from bola import Bola
from arbitro import Arbitro
from tecnico import Tecnico

class FutebolModel(Model):
    def __init__(self, duracao_jogo):
        super().__init__()
        self.grid = MultiGrid(70, 100, True)
        self.schedule = RandomActivation(self)
        self.tempo_decorrido = 0
        self.duracao_jogo = duracao_jogo
        self.running = True
        self.jogo_comecou = False
        
        # Adicionar jogadores para dois times, logicamente dividindo pela metade o total de 22 jogadores
        # Cada time é composto por 1 Goleiro, 4 Zagueiros, 4 Meias e 2 Atacantes (4-4-2)
        for i in range(0, 1):
            nome = f"Jogador_Time1_{i+1}"
            jogador = T1_Goleiro(i, self, nome, team=1)
            self.schedule.add(jogador)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height // 2)
            self.grid.place_agent(jogador, (x, y))

        for i in range(1, 5):
            nome = f"Jogador_Time1_{i+1}"
            jogador = T1_Zagueiro(i, self, nome, team=1)
            self.schedule.add(jogador)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height // 9)
            self.grid.place_agent(jogador, (x, y))

        for i in range(5, 9):
            nome = f"Jogador_Time1_{i+1}"
            jogador = T1_Meia(i, self, nome, team=1)
            self.schedule.add(jogador)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height // 4, 3 * self.grid.height // 4)
            self.grid.place_agent(jogador, (x, y))

        for i in range(9, 11):
            nome = f"Jogador_Time1_{i+1}"
            jogador = T1_Atacante(i, self, nome, team=1)
            self.schedule.add(jogador)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height // 2, self.grid.height)
            self.grid.place_agent(jogador, (x, y))

        for i in range(11, 12):
            nome = f"Jogador_Time2_{i+1}"
            jogador = T2_Goleiro(i, self, nome, team=2)
            self.schedule.add(jogador)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(9 * self.grid.height // 10, self.grid.height)
            self.grid.place_agent(jogador, (x, y))
        
        for i in range(12, 16):
            nome = f"Jogador_Time2_{i+1}"
            jogador = T2_Zagueiro(i, self, nome, team=2)
            self.schedule.add(jogador)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height // 2, self.grid.height)
            self.grid.place_agent(jogador, (x, y))

        for i in range(16, 20):
            nome = f"Jogador_Time2_{i+1}"
            jogador = T2_Meia(i, self, nome, team=2)
            self.schedule.add(jogador)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height // 4, 3 * self.grid.height // 4)
            self.grid.place_agent(jogador, (x, y))

        for i in range(20, 2):
            nome = f"Jogador_Time2_{i+1}"
            jogador = T2_Atacante(i, self, nome, team=2)
            self.schedule.add(jogador)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height // 2)
            self.grid.place_agent(jogador, (x, y))

        # Adicionar bola
        bola = Bola(22, self)
        self.schedule.add(bola)
        self.grid.place_agent(bola, (35, 50))
        
        # Adicionar árbitro
        arbitro = Arbitro(23, self, "Árbitro Principal")
        self.schedule.add(arbitro)
        self.grid.place_agent(arbitro, (69, 50))

        # Adicionar técnicos
        tecnico1 = Tecnico(24, self, "Técnico Time 1")
        tecnico2 = Tecnico(25, self, "Técnico Time 2")
        self.schedule.add(tecnico1)
        self.schedule.add(tecnico2)
        self.grid.place_agent(tecnico1, (0, 1))
        self.grid.place_agent(tecnico2, (0, 2))

    def step(self):
        self.schedule.step()
        self.tempo_decorrido += 1
        if not self.jogo_comecou and self.tempo_decorrido > 0:
            self.jogo_comecou = True
        print(f"Tempo decorrido: {self.tempo_decorrido} minuto(s)")
        if self.tempo_decorrido >= self.duracao_jogo:
            self.running = False

    def get_agent_positions(self):
        agent_positions = {
            "Jogador_time1": [],
            "Jogador_time2": [],
            "Bola": [],
            "Arbitro": []
        }
        for agent in self.schedule.agents:
            if isinstance(agent, Jogador):
                if agent.team == 1:
                    agent_positions["Jogador_time1"].append(agent.pos)
                else:
                    agent_positions["Jogador_time2"].append(agent.pos)
            elif isinstance(agent, Bola):
                agent_positions["Bola"].append(agent.pos)
            elif isinstance(agent, Arbitro):
                agent_positions["Arbitro"].append(agent.pos)
        return agent_positions
