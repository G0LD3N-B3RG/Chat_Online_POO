# tests/test_mensagem.py
from src.models.mensagem import Mensagem
from src.models.usuario import Usuario
from datetime import datetime


def test_criacao_mensagem():
    usuario = Usuario("Alice")
    conteudo = "Olá, mundo!"
    msg = Mensagem(conteudo, usuario)

    assert msg.conteudo == conteudo
    assert msg.remetente == usuario

    # Verifica formato do timestamp (HH:MM:SS)
    try:
        datetime.strptime(msg.timestamp, "%H:%M:%S")
    except ValueError:
        assert False, "Timestamp não está no formato HH:MM:SS"
