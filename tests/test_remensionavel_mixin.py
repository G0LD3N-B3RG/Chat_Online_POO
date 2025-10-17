# tests/test_redimensionavel_mixin.py
from unittest.mock import MagicMock
from src.gui.redimensionavel_mixin import RedimensionavelMixin


class DummyApp(RedimensionavelMixin):
    def __init__(self):
        self.root = MagicMock()


def test_permitir_redimensionamento_chama_resizable():
    app = DummyApp()
    app.permitir_redimensionamento()
    app.root.resizable.assert_called_once_with(True, True)
