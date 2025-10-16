# tests/test_chat.py

import pytest
from src.models.chat import Chat
from src.models.usuario import Usuario
from src.models.mensagem import Mensagem

def test_criacao_chat():
    chat = Chat()
    
    # Verifica se listas estão vazias ao criar o chat
    assert chat.usuarios == []
    assert chat.mensagens == []

def test_adicionar_usuario():
    chat = Chat()
    usuario = Usuario("Gabriel")
    
    chat.adicionar_usuario(usuario)
    
    # Verifica se o usuário foi adicionado
    assert len(chat.usuarios) == 1
    assert chat.usuarios[0].nome == "Gabriel"

def test_adicionar_mensagem():
    chat = Chat()
    usuario = Usuario("Gabriel")
    chat.adicionar_usuario(usuario)
    
    mensagem = Mensagem("Olá!", usuario)
    chat.adicionar_mensagem(mensagem)
    
    # Verifica se a mensagem foi adicionada
    assert len(chat.mensagens) == 1
    assert chat.mensagens[0].conteudo == "Olá!"
    assert chat.mensagens[0].remetente.nome == "Gabriel"
