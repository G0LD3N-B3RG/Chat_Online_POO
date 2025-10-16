# controlador.py
import socket
import threading
import json
from src.models import Usuario, Mensagem
from src.GUI import JanelaLogin, JanelaChat


class ControladorChat:
    def __init__(self):
        self.usuario = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.janela_login = JanelaLogin(self)

    def iniciar(self):
        self.janela_login.iniciar()

    def iniciar_chat(self, nome_usuario):
        self.usuario = Usuario(nome_usuario)
        self.socket.connect(('localhost', 12345))
        threading.Thread(target=self.ouvir_mensagens, daemon=True).start()

        self.janela_chat = JanelaChat(self.usuario, self)
        self.janela_chat.iniciar()

    def enviar_mensagem(self, conteudo):
        mensagem = Mensagem(conteudo, self.usuario)
        try:
            # Exibe imediatamente para o próprio cliente
            self.janela_chat.exibir_mensagem(mensagem)

            # Envia para o servidor
            self.socket.sendall(json.dumps({
                'nome': mensagem.remetente.nome,
                'conteudo': mensagem.conteudo,
                'timestamp': mensagem.timestamp
            }).encode('utf-8'))
        except Exception as e:
            print("Erro ao enviar mensagem:", e)

    def ouvir_mensagens(self):
        while True:
            try:
                dados = self.socket.recv(1024)
                if not dados:
                    break
                mensagem = json.loads(dados.decode('utf-8'))
                class Remetente: nome = mensagem['nome']
                msg = Mensagem(mensagem['conteudo'], Remetente())
                msg.timestamp = mensagem['timestamp']
                self.janela_chat.exibir_mensagem(msg)
            except:
                break
