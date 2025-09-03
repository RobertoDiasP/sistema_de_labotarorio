import tkinter as tk
from tkinter import messagebox
from janelas.nematologia import JanelaNematologia
from janelas.fitopatologia import JanelaFitopatologia
from janelas.entomologia import JanelaEntomologia
from janelas.cadastros import JanelaCadastros

class SistemaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Laboratório")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        self.criar_tela_principal()

    def criar_tela_principal(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)

        # Título
        titulo = tk.Label(main_frame,
                          text="SISTEMA DE LABORATÓRIO",
                          font=('Arial', 18, 'bold'),
                          bg='#f0f0f0',
                          fg='#2c3e50')
        titulo.pack(pady=(0, 30))

        # Frame para os botões
        botoes_frame = tk.Frame(main_frame, bg='#f0f0f0')
        botoes_frame.pack(fill='both', expand=True)

        # Botões grandes
        botoes = [
            ("NEMATOLOGIA", "#3498db", self.abrir_nematologia),
            ("FITOPATOLOGIA", "#3498db", self.abrir_fitopatologia),
            ("ENTOMOLOGIA", "#3498db", self.abrir_entomologia),
            ("CADASTROS", "#3498db", self.abrir_cadastros)
        ]

        for texto, cor, comando in botoes:
            btn = tk.Button(botoes_frame,
                            text=texto,
                            font=('Arial', 14, 'bold'),
                            bg=cor,
                            fg='white',
                            relief='raised',
                            borderwidth=3,
                            width=20,
                            height=3,
                            command=comando,
                            cursor='hand2')
            btn.pack(pady=10, fill='x')

        # Botão Sair
        btn_sair = tk.Button(main_frame,
                             text="SAIR",
                             font=('Arial', 12, 'bold'),
                             bg='#7f8c8d',
                             fg='white',
                             command=self.root.quit,
                             width=15,
                             height=2)
        btn_sair.pack(pady=20)

    def abrir_nematologia(self):
        JanelaNematologia(self.root)

    def abrir_fitopatologia(self):
        JanelaFitopatologia(self.root)

    def abrir_entomologia(self):
        JanelaEntomologia(self.root)

    def abrir_cadastros(self):
        JanelaCadastros(self.root)