# tests/test_janela_chat.py
import pytest
from unittest.mock import patch, MagicMock
from src.gui.janela_chat import JanelaChat
from src.models.usuario import Usuario


@patch("src.gui.janela_chat.tk.Tk")
@patch("src.gui.janela_chat.scrolledtext.ScrolledText")
def test_janela_chat_inicializa_componentes(mock_scrolled, mock_tk):
    """Verifica inicialização e configuração da janela de chat."""
    mock_root = MagicMock()
    mock_tk.return_value = mock_root
    mock_scrolled.return_value = MagicMock()

    usuario = Usuario("Alice")
    controlador = MagicMock()
    janela = JanelaChat(usuario, controlador)

    mock_root.title.assert_called_once_with("Chat - Alice")
    mock_root.geometry.assert_called_once_with("600x400")
    mock_root.resizable.assert_called_once_with(True, True)

    assert hasattr(janela, "texto_chat")
    assert hasattr(janela, "entrada_mensagem")
    assert hasattr(janela, "frame_chat")
    assert hasattr(janela, "frame_input")


@patch("src.gui.janela_chat.tk.Tk")
@patch("src.gui.janela_chat.scrolledtext.ScrolledText")
def test_exibir_mensagem(mock_scrolled, mock_tk):
    """Testa se exibir_mensagem insere texto corretamente no chat."""
    mock_root = MagicMock()
    mock_tk.return_value = mock_root
    mock_text = MagicMock()
    mock_scrolled.return_value = mock_text

    usuario = Usuario("Alice")
    controlador = MagicMock()
    janela = JanelaChat(usuario, controlador)

    mensagem = MagicMock()
    mensagem.timestamp = "10:00:00"
    mensagem.remetente.nome = "Alice"
    mensagem.conteudo = "Olá!"

    janela.exibir_mensagem(mensagem)

    mock_text.config.assert_any_call(state='normal')
    mock_text.insert.assert_called_once()
    mock_text.config.assert_any_call(state='disabled')
    mock_text.yview.assert_called_once()


@patch("src.gui.janela_chat.tk.Tk")
@patch("src.gui.janela_chat.scrolledtext.ScrolledText")
def test_enviar_mensagem_com_conteudo(mock_scrolled, mock_tk):
    """Verifica envio de mensagem quando há texto."""
    mock_root = MagicMock()
    mock_tk.return_value = mock_root
    mock_scrolled.return_value = MagicMock()

    usuario = Usuario("Bob")
    controlador = MagicMock()
    janela = JanelaChat(usuario, controlador)

    janela.entrada_mensagem.get = MagicMock(return_value="Oi!")
    janela.entrada_mensagem.delete = MagicMock()

    janela.enviar_mensagem(event=None)

    janela.entrada_mensagem.delete.assert_called_once()
    controlador.enviar_mensagem.assert_called_once_with("Oi!")


@patch("src.gui.janela_chat.tk.Tk")
@patch("src.gui.janela_chat.scrolledtext.ScrolledText")
def test_enviar_mensagem_sem_conteudo(mock_scrolled, mock_tk):
    """Garante que nada acontece se o campo estiver vazio."""
    mock_root = MagicMock()
    mock_tk.return_value = mock_root
    mock_scrolled.return_value = MagicMock()

    usuario = Usuario("Carol")
    controlador = MagicMock()
    janela = JanelaChat(usuario, controlador)

    janela.entrada_mensagem.get = MagicMock(return_value="")
    janela.entrada_mensagem.delete = MagicMock()

    janela.enviar_mensagem(event=None)

    janela.entrada_mensagem.delete.assert_not_called()
    controlador.enviar_mensagem.assert_not_called()
