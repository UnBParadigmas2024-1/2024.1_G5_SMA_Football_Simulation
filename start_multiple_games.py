import multiprocessing
import os

def run_game_instance(instance_id):
    os.system(f"python3 run_game.py {instance_id}")

if __name__ == "__main__":
    num_instances = 4  
    processes = []

    for i in range(num_instances):
        p = multiprocessing.Process(target=run_game_instance, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
