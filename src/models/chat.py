# modelos/chat.py
class Chat:
    def __init__(self):
        self.usuarios = []
        self.mensagens = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def adicionar_mensagem(self, mensagem):
        self.mensagens.append(mensagem)
