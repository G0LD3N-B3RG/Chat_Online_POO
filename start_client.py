# start_client.py
import subprocess
import sys
import time

NUM_CLIENTES = 3  # Número de janelas de clientes que deseja abrir

for i in range(NUM_CLIENTES):
    print(f"Abrindo cliente {i+1}...")
    subprocess.Popen([sys.executable, "main.py"])
    time.sleep(0.5)  # Pequeno delay para evitar sobrecarga
