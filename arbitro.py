from mesa import Agent

class Arbitro(Agent):
    def __init__(self, unique_id, model, nome):
        super().__init__(unique_id, model)
        self.nome = nome
        self.times_apitou = set() 
        self.inicio_apitou = False  
        self.fim_apitou = False

    def step(self):
        self.apitar()

    def apitar(self):
        tempo_atual = self.model.tempo_decorrido

        if tempo_atual == 0 and not self.inicio_apitou:
            print(f"{self.nome} apitou o início do jogo!!!")
            self.inicio_apitou = True  
            self.times_apitou.add(tempo_atual)

        if tempo_atual == 89 and not self.fim_apitou:
            print(f"{self.nome} apitou o fim do jogo!!!")
            self.fim_apitou = True  
            self.times_apitou.add(tempo_atual)

        momentos_de_apito = [45, 90]
        if tempo_atual in momentos_de_apito and tempo_atual not in self.times_apitou:
            self.times_apitou.add(tempo_atual)
            if tempo_atual == 45:
                print(f"{self.nome} apitou o fim do primeiro tempo.")
            elif tempo_atual == 90:
                print(f"{self.nome} apitou o fim do jogo.")

 
