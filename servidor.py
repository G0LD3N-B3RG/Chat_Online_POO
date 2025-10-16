# servidor.py
import socket
import threading
import json
clientes = []


def broadcast(mensagem, remetente_socket):
    for cliente in clientes:
        if cliente != remetente_socket:
            try:
                cliente.sendall(mensagem)
            except:
                clientes.remove(cliente)


def lidar_com_cliente(cliente_socket, endereco):
    print(f"[+] Novo cliente conectado: {endereco}")
    while True:
        try:
            dados = cliente_socket.recv(1024)
            if not dados:
                break
            broadcast(dados, cliente_socket)
        except:
            break
    print(f"[-] Cliente desconectado: {endereco}")
    clientes.remove(cliente_socket)
    cliente_socket.close()


def iniciar_servidor(host='127.0.0.1', porta=12345):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    print(f"[SERVIDOR] Escutando em {host}:{porta}...")

    while True:
        cliente_socket, endereco = servidor.accept()
        clientes.append(cliente_socket)
        thread = threading.Thread(target=lidar_com_cliente, args=(cliente_socket, endereco))
        thread.start()


if __name__ == '__main__':
    iniciar_servidor()

