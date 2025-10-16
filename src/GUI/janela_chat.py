# gui/janela_chat.py
import tkinter as tk
from tkinter import scrolledtext
from .janela_base import JanelaBase
from .redimensionavel_mixin import RedimensionavelMixin


class JanelaChat(JanelaBase, RedimensionavelMixin):
    def __init__(self, usuario, controlador):
        super().__init__()
        self.usuario = usuario
        self.controlador = controlador
        self.root.title(f"Chat - {usuario.nome}")
        self.root.geometry("600x400")
        self.permitir_redimensionamento()

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_columnconfigure(0, weight=1)

        self.frame_chat = tk.Frame(self.root)
        self.frame_chat.grid(row=0, column=0, sticky="nsew")

        self.texto_chat = scrolledtext.ScrolledText(self.frame_chat, state='disabled')
        self.texto_chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.frame_input = tk.Frame(self.root)
        self.frame_input.grid(row=1, column=0, sticky="ew")

        self.entrada_mensagem = tk.Entry(self.frame_input)
        self.entrada_mensagem.pack(padx=10, pady=10, fill=tk.X, expand=True)
        self.entrada_mensagem.bind("<Return>", self.enviar_mensagem)

    def exibir_mensagem(self, mensagem):
        self.texto_chat.config(state='normal')
        self.texto_chat.insert(tk.END, f"[{mensagem.timestamp}] {mensagem.remetente.nome}: {mensagem.conteudo}\n")
        self.texto_chat.config(state='disabled')
        self.texto_chat.yview(tk.END)

    def enviar_mensagem(self, event):
        conteudo = self.entrada_mensagem.get()
        if conteudo:
            self.entrada_mensagem.delete(0, tk.END)
            self.controlador.enviar_mensagem(conteudo)
