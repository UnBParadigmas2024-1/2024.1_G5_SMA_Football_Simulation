import time
from futebol_model import FutebolModel

duracao_jogo = 90

model = FutebolModel(duracao_jogo)  
model = FutebolModel(duracao_jogo)  

while model.running:
    model.step()
    time.sleep(0.5)  

print("O jogo acabou!")
