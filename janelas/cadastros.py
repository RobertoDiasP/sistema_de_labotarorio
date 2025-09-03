import tkinter as tk
import sys
import os

# Adiciona o diretório pai ao path para importar subjanelas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from subjanelas.clientes import JanelaClientes
from subjanelas.produtos_quimicos import JanelaProdutosQuimicos
from subjanelas.epis import JanelaEPIs
from subjanelas.itens import JanelaItens


class JanelaCadastros:
    def __init__(self, parent):
        self.parent = parent
        self.cor = "white"
        self.criar_janela()

    def criar_janela(self):
        self.janela = tk.Toplevel(self.parent)
        self.janela.title("Sistema de Cadastros")
        self.janela.geometry("600x500")
        self.janela.configure(bg=self.cor)
        self.janela.resizable(True, True)

        self.janela.transient(self.parent)
        self.janela.grab_set()

        self.criar_conteudo()

    def criar_conteudo(self):
        frame_conteudo = tk.Frame(self.janela, bg=self.cor, padx=20, pady=20)
        frame_conteudo.pack(fill='both', expand=True)

        # Título
        lbl_titulo = tk.Label(frame_conteudo,
                              text="SISTEMA DE CADASTROS",
                              font=('Arial', 18, 'bold'),
                              bg=self.cor,
                              fg='#2c3e50')
        lbl_titulo.pack(pady=(0, 30))

        # Frame para os botões de cadastro
        botoes_frame = tk.Frame(frame_conteudo, bg=self.cor)
        botoes_frame.pack(fill='both', expand=True)

        # Botões para diferentes tipos de cadastro
        botoes_cadastro = [
            ("👥 CLIENTES", "#3498db", self.abrir_clientes),
            ("🧪 PRODUTOS QUÍMICOS", "#27ae60", self.abrir_produtos_quimicos),
            ("🛡️ EPIs", "#f39c12", self.abrir_epis),
            ("📦 ITENS EM GERAL", "#9b59b6", self.abrir_itens)
        ]

        for texto, cor, comando in botoes_cadastro:
            btn = tk.Button(botoes_frame,
                            text=texto,
                            font=('Arial', 12, 'bold'),
                            bg=cor,
                            fg='white',
                            relief='raised',
                            borderwidth=2,
                            width=25,
                            height=2,
                            command=comando,
                            cursor='hand2')
            btn.pack(pady=10)

        # Botão Voltar
        btn_voltar = tk.Button(frame_conteudo,
                               text="VOLTAR",
                               font=('Arial', 12, 'bold'),
                               bg='#7f8c8d',
                               fg='white',
                               command=self.janela.destroy,
                               width=15,
                               height=1)
        btn_voltar.pack(side='bottom', pady=20)

    def abrir_clientes(self):
        JanelaClientes(self.janela)

    def abrir_produtos_quimicos(self):
        JanelaProdutosQuimicos(self.janela)

    def abrir_epis(self):
        JanelaEPIs(self.janela)

    def abrir_itens(self):
        JanelaItens(self.janela)