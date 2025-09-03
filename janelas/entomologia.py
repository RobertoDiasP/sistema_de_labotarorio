import tkinter as tk
from tkinter import ttk


class JanelaEntomologia:
    def __init__(self, parent):
        self.parent = parent
        self.cor = "white"
        self.criar_janela()

    def criar_janela(self):
        self.janela = tk.Toplevel(self.parent)
        self.janela.title("Entomologia")
        self.janela.geometry("500x400")
        self.janela.configure(bg=self.cor)
        self.janela.resizable(True, True)

        self.janela.transient(self.parent)
        self.janela.grab_set()

        self.criar_conteudo()

    def criar_conteudo(self):
        frame_conteudo = tk.Frame(self.janela, bg=self.cor, padx=20, pady=20)
        frame_conteudo.pack(fill='both', expand=True)

        lbl_titulo = tk.Label(frame_conteudo,
                              text="ENTOMOLOGIA",
                              font=('Arial', 16, 'bold'),
                              bg=self.cor,
                              fg='black')
        lbl_titulo.pack(pady=20)

        conteudo = tk.Label(frame_conteudo,
                            text="Módulo de Entomologia\n\n"
                                 "• Identificação de insetos\n"
                                 "• Controle de pragas\n"
                                 "• Monitoramento populacional\n"
                                 "• Manejo integrado",
                            font=('Arial', 12),
                            bg=self.cor,
                            fg='black',
                            justify='left')
        conteudo.pack(pady=20)

        btn_voltar = tk.Button(frame_conteudo,
                               text="VOLTAR",
                               font=('Arial', 12, 'bold'),
                               bg='#2c3e50',
                               fg='white',
                               command=self.janela.destroy)
        btn_voltar.pack(side='bottom', pady=20)