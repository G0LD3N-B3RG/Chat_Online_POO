# models/usuario.py
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.mensagens_enviadas = []
