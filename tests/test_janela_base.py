# tests/test_janela_base.py

import tkinter as tk
from src.gui.janela_base import JanelaBase

def test_criacao_janela_base():
    janela = JanelaBase()
    
    # Oculta a janela para não aparecer na tela durante o teste
    janela.root.withdraw()
    
    # Verifica se o root é uma instância de Tk
    assert isinstance(janela.root, tk.Tk)
    
    # Verifica se a janela existe
    assert janela.root.winfo_exists() == 1
    
    # Fecha a janela após o teste
    janela.root.destroy()
