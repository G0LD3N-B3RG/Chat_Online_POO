# tests/test_controlador.py

import pytest
import json
from src.controlador import ControladorChat
from src.models import Usuario, Mensagem

class DummySocket:
    """Socket fake para testar envio de mensagens"""
    def __init__(self):
        self.sent_data = []

    def connect(self, endereco):
        self.endereco = endereco

    def sendall(self, dados):
        self.sent_data.append(dados)

    def recv(self, bufsize):
        # Retorna nada para simular fim de conexão
        return b''

def test_iniciar_chat_e_enviar_mensagem(monkeypatch):
    # Substitui o socket real por DummySocket
    dummy_socket = DummySocket()
    
    # Substitui as janelas por versões dummy para não abrir GUI
    class DummyJanelaLogin:
        def iniciar(self): pass

    class DummyJanelaChat:
        def __init__(self, usuario, controlador):
            self.usuario = usuario
            self.controlador = controlador
            self.mensagens_exibidas = []

        def exibir_mensagem(self, mensagem):
            self.mensagens_exibidas.append(mensagem)

        def iniciar(self): pass

    # Patches
    monkeypatch.setattr("src.controlador.socket.socket", lambda *args, **kwargs: dummy_socket)
    monkeypatch.setattr("src.controlador.JanelaLogin", lambda ctrl: DummyJanelaLogin())
    monkeypatch.setattr("src.controlador.JanelaChat", lambda usuario, ctrl: DummyJanelaChat(usuario, ctrl))

    # Cria controlador
    controlador = ControladorChat()
    
    # Inicia chat
    controlador.iniciar_chat("Gabriel")
    
    # Verifica usuário
    assert controlador.usuario.nome == "Gabriel"
    
    # Envia mensagem
    controlador.enviar_mensagem("Olá mundo!")

    # Verifica que a mensagem foi exibida na janela dummy
    assert len(controlador.janela_chat.mensagens_exibidas) == 1
    assert controlador.janela_chat.mensagens_exibidas[0].conteudo == "Olá mundo!"

    # Verifica que o socket "enviou" os dados
    sent_json = json.loads(dummy_socket.sent_data[0].decode('utf-8'))
    assert sent_json['nome'] == "Gabriel"
    assert sent_json['conteudo'] == "Olá mundo!"
