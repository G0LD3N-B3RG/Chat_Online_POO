# tests/test_usuario.py

import pytest
from src.models.usuario import Usuario  # ajuste o import conforme sua estrutura de pastas

def test_criacao_usuario():
    nome = "Gabriel"
    usuario = Usuario(nome)
    
    # Verifica se o nome foi atribuído corretamente
    assert usuario.nome == nome
    
    # Verifica se a lista de mensagens enviadas está vazia
    assert usuario.mensagens_enviadas == []

def test_adicionar_mensagem():
    usuario = Usuario("Gabriel")
    
    # Simulando o envio de uma mensagem
    usuario.mensagens_enviadas.append("Olá, mundo!")
    
    # Verifica se a mensagem foi adicionada
    assert usuario.mensagens_enviadas == ["Olá, mundo!"]
