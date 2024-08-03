import matplotlib.pyplot as plt
import time
from futebol_model import FutebolModel

def plot_positions(ax, model):
    ax.clear()
    
    agent_positions = model.get_agent_positions()
    
    ax.set_xlim(0, model.grid.width)
    ax.set_ylim(0, model.grid.height)
    
    for pos in agent_positions["Jogador"]:
        x, y = pos
        ax.scatter(x, y, c='blue', marker='o', label='Jogador')

    for pos in agent_positions["Bola"]:
        x, y = pos
        ax.scatter(x, y, c='black', marker='x', label='Bola')

    for pos in agent_positions["Arbitro"]:
        x, y = pos
        ax.scatter(x, y, c='red', marker='s', label='Arbitro')

    ax.set_title(f'Tempo decorrido: {model.tempo_decorrido} minuto(s)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

def main():
    duracao_jogo = 90
    model = FutebolModel(duracao_jogo)
    
    plt.ion()  # Modo interativo
    fig, ax = plt.subplots(figsize=(10, 10))
    
    while model.running:
        model.step()
        plot_positions(ax, model)
        plt.draw()
        plt.pause(0.5)  # Pause para visualizar a mudança de estado

    plt.ioff()  # Desativa o modo interativo
    plt.show()
    print("O jogo acabou!")

if __name__ == "__main__":
    main()
