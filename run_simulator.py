
from futebol_model import FutebolModel
import matplotlib.pyplot as plt
import time

def plot_positions(ax, model):
    ax.clear()
    
    agent_positions = model.get_agent_positions()
    
    ax.set_xlim(0, model.grid.width)
    ax.set_ylim(0, model.grid.height)

    for pos in agent_positions["Jogador_T1_goleiro"]:
        x, y = pos
        ax.scatter(x, y, c='magenta', marker="D", label='Jogador Time 1')
        ax.text(x, y+1, 'Goleiro_1', fontsize=8, ha='center')
        
    for pos in agent_positions["Jogador_T2_goleiro"]:
        x, y = pos
        ax.scatter(x, y, c='purple', marker="D", label='Jogador Time 1')
        ax.text(x, y+1, 'Goleiro_2', fontsize=8, ha='center')

    for pos in agent_positions["Jogador_T1_zagueiro"]:
        x, y = pos
        ax.scatter(x, y, c='blue', marker='o', label='Jogador Time 1')
        ax.text(x, y+1, 'T1_zagueiro', fontsize=8, ha='center')
    
    for pos in agent_positions["Jogador_T1_meia"]:
        x, y = pos
        ax.scatter(x, y, c='blue', marker='o', label='Jogador Time 1')
        ax.text(x, y+1, 'T1_meia', fontsize=8, ha='center')
        
    for pos in agent_positions["Jogador_T1_atacante"]:
        x, y = pos
        ax.scatter(x, y, c='blue', marker='o', label='Jogador Time 1')
        ax.text(x, y+1, 'T1_atacante', fontsize=8, ha='center')
    

    for pos in agent_positions["Jogador_T2_zagueiro"]:
        x, y = pos
        ax.scatter(x, y, c='red', marker='o', label='Jogador Time 2')
        ax.text(x, y+1, 'T2_zagueiro', fontsize=8, ha='center')

    for pos in agent_positions["Jogador_T2_meia"]:
        x, y = pos
        ax.scatter(x, y, c='red', marker='o', label='Jogador Time 2')
        ax.text(x, y+1, 'T2_meia', fontsize=8, ha='center')

    for pos in agent_positions["Jogador_T2_atacante"]:
        x, y = pos
        ax.scatter(x, y, c='red', marker='o', label='Jogador Time 2')
        ax.text(x, y+1, 'T2_atacante', fontsize=8, ha='center')

    for pos in agent_positions["Bola"]:
        x, y = pos
        ax.scatter(x, y, c='black', marker='x', label='Bola')
        ax.text(x, y+1, 'Bola', fontsize=8, ha='center')

    for pos in agent_positions["Arbitro"]:
        x, y = pos
        ax.scatter(x, y, c='green', marker='s', label='Arbitro')

   

    ax.set_title(f'Tempo decorrido: {model.tempo_decorrido} minuto(s)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

def main():
    duracao_jogo = 90
    model = FutebolModel(duracao_jogo)
    
    plt.ion()  # Modo interativo ligado
    fig, ax = plt.subplots(figsize=(7, 10))
    
    def on_close(event):
        model.running = False
    
    fig.canvas.mpl_connect('close_event', on_close)
    
    while model.running:
        model.step()
        plot_positions(ax, model)
        plt.draw()
        plt.pause(0.5)  # Pausa de 0.5 segundos para animação

    plt.ioff()  # Modo interativo desligado
    plt.show()
    print("O jogo acabou!")

if __name__ == "__main__":
    main()
