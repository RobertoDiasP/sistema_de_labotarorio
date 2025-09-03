import tkinter as tk
from tkinter import ttk, messagebox


class JanelaClientes:
    def __init__(self, parent):
        self.parent = parent
        self.cor = "white"
        self.criar_janela()

    def criar_janela(self):
        self.janela = tk.Toplevel(self.parent)
        self.janela.title("Cadastro de Clientes")
        self.janela.geometry("500x500")
        self.janela.configure(bg=self.cor)

        self.janela.transient(self.parent)
        self.janela.grab_set()

        self.criar_formulario()

    def criar_formulario(self):
        frame_principal = tk.Frame(self.janela, bg=self.cor, padx=20, pady=20)
        frame_principal.pack(fill='both', expand=True)

        # Título
        lbl_titulo = tk.Label(frame_principal,
                              text="CADASTRO DE CLIENTES",
                              font=('Arial', 16, 'bold'),
                              bg=self.cor,
                              fg='black')
        lbl_titulo.pack(pady=(0, 20))

        # Formulário
        frame_form = tk.Frame(frame_principal, bg=self.cor)
        frame_form.pack(fill='x', pady=10)

        campos = [
            ("Nome Completo:", 0),
            ("CPF/CNPJ:", 1),
            ("Telefone:", 2),
            ("Email:", 3),
            ("Endereço:", 4),
            ("Cidade:", 5),
            ("Estado:", 6)
        ]

        self.entries = []
        for texto, linha in campos:
            lbl = tk.Label(frame_form, text=texto, bg=self.cor, fg='black',
                           font=('Arial', 10), anchor='w')
            lbl.grid(row=linha, column=0, sticky='w', pady=5, padx=5)

            entry = tk.Entry(frame_form, width=30, font=('Arial', 10))
            entry.grid(row=linha, column=1, pady=5, padx=5)
            self.entries.append(entry)

        # Botões
        frame_botoes = tk.Frame(frame_principal, bg=self.cor)
        frame_botoes.pack(pady=20)

        btn_salvar = tk.Button(frame_botoes,
                               text="SALVAR CLIENTE",
                               bg='#27ae60',
                               fg='white',
                               font=('Arial', 10, 'bold'),
                               command=self.salvar_cliente,
                               width=15)
        btn_salvar.pack(side='left', padx=5)

        btn_limpar = tk.Button(frame_botoes,
                               text="LIMPAR",
                               bg='#f39c12',
                               fg='white',
                               font=('Arial', 10, 'bold'),
                               command=self.limpar_campos,
                               width=10)
        btn_limpar.pack(side='left', padx=5)

        btn_voltar = tk.Button(frame_botoes,
                               text="VOLTAR",
                               bg='#7f8c8d',
                               fg='white',
                               font=('Arial', 10, 'bold'),
                               command=self.janela.destroy,
                               width=10)
        btn_voltar.pack(side='left', padx=5)

    def salvar_cliente(self):
        dados = [entry.get().strip() for entry in self.entries]
        if all(dados[:4]):  # Pelo menos nome, CPF, telefone e email
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Preencha os campos obrigatórios: Nome, CPF, Telefone e Email!")

    def limpar_campos(self):
        for entry in self.entries:
            entry.delete(0, tk.END)