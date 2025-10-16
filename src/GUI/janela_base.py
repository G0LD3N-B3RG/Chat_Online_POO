# gui/janela_base.py
import tkinter as tk


class JanelaBase:
    def __init__(self):
        self.root = tk.Tk()

    def iniciar(self):
        self.root.mainloop()
