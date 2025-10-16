# tests/test_janela_chat.py

import tkinter as tk
from src.gui.janela_chat import JanelaChat
from src.models.usuario import Usuario
from src.models.mensagem import Mensagem

class ControladorDummy:
    def __init__(self):
        self.mensagens_enviadas = []

    def enviar_mensagem(self, conteudo):
        self.mensagens_enviadas.append(conteudo)

def test_janela_chat_inicializacao():
    usuario = Usuario("Gabriel")
    controlador = ControladorDummy()
    
    janela = JanelaChat(usuario, controlador)
    janela.root.withdraw()  # não mostra a janela
    
    # Verifica título e geometria
    assert janela.root.title() == f"Chat - {usuario.nome}"
    assert janela.root.winfo_geometry() == "600x400"
    
    # Verifica se os widgets foram criados
    assert janela.entrada_mensagem is not None
    assert janela.texto_chat is not None

def test_enviar_mensagem():
    usuario = Usuario("Gabriel")
    controlador = ControladorDummy()
    
    janela = JanelaChat(usuario, controlador)
    janela.root.withdraw()
    
    # Simula digitar mensagem
    janela.entrada_mensagem.insert(0, "Olá mundo!")
    
    # Simula pressionar Enter
    janela.enviar_mensagem(None)
    
    # Verifica se a entrada foi limpa
    assert janela.entrada_mensagem.get() == ""
    
    # Verifica se a mensagem foi registrada no controlador
    assert controlador.mensagens_enviadas == ["Olá mundo!"]

def test_exibir_mensagem():
    usuario = Usuario("Gabriel")
    controlador = ControladorDummy()
    
    janela = JanelaChat(usuario, controlador)
    janela.root.withdraw()
    
    # Cria uma mensagem e exibe
    mensagem = Mensagem("Teste mensagem", usuario)
    janela.exibir_mensagem(mensagem)
    
    # Verifica se o texto da mensagem aparece no ScrolledText
    texto = janela.texto_chat.get("1.0", tk.END)
    assert "Teste mensagem" in texto
    assert usuario.nome in texto
