# models/mensagem.py
from datetime import datetime


class Mensagem:
    def __init__(self, conteudo, remetente):
        self.conteudo = conteudo
        self.remetente = remetente
        self.timestamp = datetime.now().strftime("%H:%M:%S")