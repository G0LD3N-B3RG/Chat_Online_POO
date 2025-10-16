# tests/test_janela_login.py

import tkinter as tk
from src.gui.janela_login import JanelaLogin

class ControladorDummy:
    def __init__(self):
        self.usuario_iniciado = None

    def iniciar_chat(self, nome):
        self.usuario_iniciado = nome

def test_janela_login():
    # Cria o controlador real
    controlador = ControladorDummy()
    
    # Cria a janela
    janela = JanelaLogin(controlador)
    
    # Evita que a janela apareça na tela durante o teste
    janela.root.withdraw()
    
    # Simula digitar nome
    janela.entrada_usuario.insert(0, "Gabriel")
    
    # Chama método de entrar no chat
    janela.entrar_chat()
    
    # Verifica se o método do controlador foi chamado corretamente
    assert controlador.usuario_iniciado == "Gabriel"
    
    # Verifica se a janela foi destruída
    assert not janela.root.winfo_exists()
