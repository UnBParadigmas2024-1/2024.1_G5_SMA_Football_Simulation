import sys
import time
from futebol_model import FutebolModel

def start_game(instance_id):
    print(f"Iniciando o jogo na instância {instance_id}...")
    
    duracao_jogo = 90

    model = FutebolModel(duracao_jogo)

    while model.running:
        model.step()
        time.sleep(0.5) 

    print(f"Instância {instance_id}: O jogo acabou!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        instance_id = sys.argv[1]
        start_game(instance_id)
    else:
        print("Por favor, forneça um ID de instância.")
