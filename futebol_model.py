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
        
        # Time 1 (defendendo na parte inferior do campo)
        
        # Goleiro do Time 1
        x = self.grid.width // 2
        y = 7  # Próximo à linha de fundo inferior
        jogador = T1_Goleiro(0, self, nome="Goleiro_T1", team=1)
        self.schedule.add(jogador)
        self.grid.place_agent(jogador, (x, y))

        # Zagueiros do Time 1
        zagueiros_posicoes = [(self.grid.width // 7, 20),
                              (self.grid.width // 2 - 10, 15),
                              (self.grid.width // 2 + 10, 15),
                              (3 * self.grid.width // 4 + 8, 20)]
        for i, pos in enumerate(zagueiros_posicoes):
            jogador = T1_Zagueiro(i+1, self, nome=f"Zagueiro_T1_{i+1}", team=1)
            self.schedule.add(jogador)
            self.grid.place_agent(jogador, pos)

        # Meio-campistas do Time 1
        meias_posicoes = [(self.grid.width // 4, 35),
                          (self.grid.width // 2 - 5, 35),
                          (self.grid.width // 2 + 5, 35),
                          (3 * self.grid.width // 4, 35)]
        for i, pos in enumerate(meias_posicoes):
            jogador = T1_Meia(i+5, self, nome=f"Meia_T1_{i+1}", team=1)
            self.schedule.add(jogador)
            self.grid.place_agent(jogador, pos)

        # Atacantes do Time 1
        atacantes_posicoes = [(self.grid.width // 3, 45),
                              (2 * self.grid.width // 3, 45)]
        for i, pos in enumerate(atacantes_posicoes):
            jogador = T1_Atacante(i+9, self, nome=f"Atacante_T1_{i+1}", team=1)
            self.schedule.add(jogador)
            self.grid.place_agent(jogador, pos)

        
        # Goleiro do Time 2
        x = self.grid.width // 2
        y = self.grid.height - 5  # Próximo à linha de fundo superior
        jogador = T2_Goleiro(11, self, nome="Goleiro_T2", team=2)
        self.schedule.add(jogador)
        self.grid.place_agent(jogador, (x, y))

        # Zagueiros do Time 2
        zagueiros_posicoes = [(self.grid.width // 4, self.grid.height - 15),
                              (self.grid.width // 2 - 5, self.grid.height - 15),
                              (self.grid.width // 2 + 5, self.grid.height - 15),
                              (3 * self.grid.width // 4, self.grid.height - 15)]
        for i, pos in enumerate(zagueiros_posicoes):
            jogador = T2_Zagueiro(i+12, self, nome=f"Zagueiro_T2_{i+1}", team=2)
            self.schedule.add(jogador)
            self.grid.place_agent(jogador, pos)

        # Meio-campistas do Time 2
        meias_posicoes = [(self.grid.width // 4, self.grid.height - 35),
                          (self.grid.width // 2 - 5, self.grid.height - 35),
                          (self.grid.width // 2 + 5, self.grid.height - 35),
                          (3 * self.grid.width // 4, self.grid.height - 35)]
        for i, pos in enumerate(meias_posicoes):
            jogador = T2_Meia(i+16, self, nome=f"Meia_T2_{i+1}", team=2)
            self.schedule.add(jogador)
            self.grid.place_agent(jogador, pos)

        # Atacantes do Time 2
        atacantes_posicoes = [(self.grid.width // 3, self.grid.height - 45),
                              (2 * self.grid.width // 3, self.grid.height - 45)]
        for i, pos in enumerate(atacantes_posicoes):
            jogador = T2_Atacante(i+20, self, nome=f"Atacante_T2_{i+1}", team=2)
            self.schedule.add(jogador)
            self.grid.place_agent(jogador, pos)

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
            "Jogador_T1_goleiro": [],
            "Jogador_T1_zagueiro": [],
            "Jogador_T1_meia": [],
            "Jogador_T1_atacante": [],
            "Jogador_T2_goleiro": [],
            "Jogador_T2_zagueiro": [],
            "Jogador_T2_meia": [],
            "Jogador_T2_atacante": [],
            "Bola": [],
            "Arbitro": []
        }
        for agent in self.schedule.agents:
            if isinstance(agent, Jogador):
                if isinstance(agent, T1_Goleiro):
                    agent_positions["Jogador_T1_goleiro"].append(agent.pos)
                elif isinstance(agent, T2_Goleiro):
                    agent_positions["Jogador_T2_goleiro"].append(agent.pos)
                elif isinstance(agent, T1_Atacante):
                    agent_positions["Jogador_T1_atacante"].append(agent.pos)
                elif isinstance(agent, T2_Atacante):
                    agent_positions["Jogador_T2_atacante"].append(agent.pos)
                elif isinstance(agent, T1_Meia):
                    agent_positions["Jogador_T1_meia"].append(agent.pos)
                elif isinstance(agent, T2_Meia):
                    agent_positions["Jogador_T2_meia"].append(agent.pos)
                elif isinstance(agent, T1_Zagueiro):
                    agent_positions["Jogador_T1_zagueiro"].append(agent.pos)
                else:
                     agent_positions["Jogador_T2_zagueiro"].append(agent.pos)
            elif isinstance(agent, Bola):
                agent_positions["Bola"].append(agent.pos)
            elif isinstance(agent, Arbitro):
                agent_positions["Arbitro"].append(agent.pos)
        return agent_positions
