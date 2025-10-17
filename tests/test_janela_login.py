# tests/test_janela_login.py
import pytest
from unittest.mock import patch, MagicMock
from src.gui.janela_login import JanelaLogin


@patch("src.gui.janela_login.tk.Tk")
def test_janela_login_inicializa_componentes(mock_tk):
    """Verifica se a janela e seus widgets são criados corretamente."""
    mock_root = MagicMock()
    mock_tk.return_value = mock_root
    controlador = MagicMock()

    janela = JanelaLogin(controlador)

    # Checa se propriedades da janela foram configuradas
    mock_root.title.assert_called_once_with("Login")
    mock_root.geometry.assert_called_once_with("300x150")

    # Confirma se os elementos principais existem
    assert hasattr(janela, "entrada_usuario")
    assert hasattr(janela, "botao_entrar")
    assert janela.controlador == controlador


@patch("src.gui.janela_login.tk.Tk")
def test_entrar_chat_com_nome(mock_tk):
    """Confirma que ao digitar um nome, a janela fecha e inicia o chat."""
    mock_root = MagicMock()
    mock_tk.return_value = mock_root
    controlador = MagicMock()

    janela = JanelaLogin(controlador)
    janela.entrada_usuario.get = MagicMock(return_value="Alice")

    janela.entrar_chat()

    mock_root.destroy.assert_called_once()
    controlador.iniciar_chat.assert_called_once_with("Alice")


@patch("src.gui.janela_login.tk.Tk")
def test_entrar_chat_sem_nome(mock_tk):
    """Garante que nada acontece se o campo de nome estiver vazio."""
    mock_root = MagicMock()
    mock_tk.return_value = mock_root
    controlador = MagicMock()

    janela = JanelaLogin(controlador)
    janela.entrada_usuario.get = MagicMock(return_value="")

    janela.entrar_chat()

    # Nenhuma ação deve ocorrer
    mock_root.destroy.assert_not_called()
    controlador.iniciar_chat.assert_not_called()
