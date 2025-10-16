# gui/janela_login.py
import tkinter as tk
from .janela_base import JanelaBase


class JanelaLogin(JanelaBase):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.root.title("Login")
        self.root.geometry("300x150")

        self.label = tk.Label(self.root, text="Nome de usuário:")
        self.label.pack(pady=10)

        self.entrada_usuario = tk.Entry(self.root)
        self.entrada_usuario.pack(pady=5)

        self.botao_entrar = tk.Button(self.root, text="Entrar", command=self.entrar_chat)
        self.botao_entrar.pack(pady=10)

    def entrar_chat(self):
        nome = self.entrada_usuario.get()
        if nome:
            self.root.destroy()
            self.controlador.iniciar_chat(nome)
