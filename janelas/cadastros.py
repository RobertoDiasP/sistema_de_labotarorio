import tkinter as tk
from tkinter import ttk, messagebox


class JanelaCadastros:
    def __init__(self, parent):
        self.parent = parent
        self.cor = "white"
        self.entries_cadastro = []
        self.criar_janela()

    def criar_janela(self):
        self.janela = tk.Toplevel(self.parent)
        self.janela.title("Cadastros")
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
                              text="CADASTROS",
                              font=('Arial', 16, 'bold'),
                              bg=self.cor,
                              fg='black')
        lbl_titulo.pack(pady=20)

        # Frame para formulário de cadastro
        form_frame = tk.Frame(frame_conteudo, bg=self.cor)
        form_frame.pack(pady=20)

        # Campos do formulário
        campos = [
            ("Nome:", 0),
            ("Email:", 1),
            ("Telefone:", 2),
            ("Setor:", 3)
        ]

        self.entries_cadastro = []
        for texto, linha in campos:
            lbl = tk.Label(form_frame, text=texto, bg=self.cor, fg='black', font=('Arial', 10))
            lbl.grid(row=linha, column=0, sticky='w', pady=5, padx=5)

            entry = tk.Entry(form_frame, width=30, font=('Arial', 10))
            entry.grid(row=linha, column=1, pady=5, padx=5)
            self.entries_cadastro.append(entry)

        # Botão Cadastrar
        btn_cadastrar = tk.Button(form_frame,
                                  text="CADASTRAR",
                                  bg='#2c3e50',
                                  fg='white',
                                  font=('Arial', 10, 'bold'),
                                  command=self.cadastrar_usuario)
        btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=15)

        # Botão Voltar
        btn_voltar = tk.Button(frame_conteudo,
                               text="VOLTAR",
                               font=('Arial', 12, 'bold'),
                               bg='#2c3e50',
                               fg='white',
                               command=self.janela.destroy)
        btn_voltar.pack(side='bottom', pady=20)

    def cadastrar_usuario(self):
        dados = [entry.get() for entry in self.entries_cadastro]
        if all(dados):
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            for entry in self.entries_cadastro:
                entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")