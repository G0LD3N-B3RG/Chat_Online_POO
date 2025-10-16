# tests/test_redimensionavel_mixin_tkinter.py

import pytest
import tkinter as tk
from src.gui.redimensionavel_mixin import RedimensionavelMixin

class Janela(RedimensionavelMixin):
    def __init__(self):
        self.root = tk.Tk()
        # Opcional: não mostrar a janela durante o teste
        self.root.withdraw()

def test_permitir_redimensionamento_tkinter():
    janela = Janela()
    
    # Deve executar sem erros
    janela.permitir_redimensionamento()
    
    # Verifica se a janela está configurada para ser redimensionável
    largura, altura = janela.root.resizable()
    assert largura is True
    assert altura is True
    
    # Fecha a janela após o teste
    janela.root.destroy()
