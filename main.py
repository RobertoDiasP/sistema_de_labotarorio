import tkinter as tk
from tkinter import ttk, messagebox


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
        self.abrir_janela("Nematologia", "")

    def abrir_fitopatologia(self):
        self.abrir_janela("Fitopatologia", "")

    def abrir_entomologia(self):
        self.abrir_janela("Entomologia", "")

    def abrir_cadastros(self):
        self.abrir_janela("Cadastros","" )

    def abrir_janela(self, titulo, cor):
        # Criar nova janela
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title(titulo)
        nova_janela.geometry("500x400")
        nova_janela.configure(bg=cor)
        nova_janela.resizable(True, True)

        # Centralizar a janela
        nova_janela.transient(self.root)
        nova_janela.grab_set()

        # Conteúdo da janela
        frame_conteudo = tk.Frame(nova_janela, bg=cor, padx=20, pady=20)
        frame_conteudo.pack(fill='both', expand=True)

        # Título
        lbl_titulo = tk.Label(frame_conteudo,
                              text=titulo.upper(),
                              font=('Arial', 16, 'bold'),
                              bg=cor,
                              fg='white')
        lbl_titulo.pack(pady=20)

        # Conteúdo específico para cada módulo
        if titulo == "Nematologia":
            self.criar_conteudo_nematologia(frame_conteudo, cor)
        elif titulo == "Fitopatologia":
            self.criar_conteudo_fitopatologia(frame_conteudo, cor)
        elif titulo == "Entomologia":
            self.criar_conteudo_entomologia(frame_conteudo, cor)
        elif titulo == "Cadastros":
            self.criar_conteudo_cadastros(frame_conteudo, cor)

        # Botão Voltar
        btn_voltar = tk.Button(frame_conteudo,
                               text="VOLTAR",
                               font=('Arial', 12, 'bold'),
                               bg='#2c3e50',
                               fg='white',
                               command=nova_janela.destroy)
        btn_voltar.pack(side='bottom', pady=20)

    def criar_conteudo_nematologia(self, frame, cor):
        conteudo = tk.Label(frame,
                            text="Módulo de Nematologia\n\n"
                                 "• Análise de nematoides\n"
                                 "• Contagem de espécies\n"
                                 "• Relatórios de infestação\n"
                                 "• Controle e tratamento",
                            font=('Arial', 12),
                            bg=cor,
                            fg='white',
                            justify='left')
        conteudo.pack(pady=20)

    def criar_conteudo_fitopatologia(self, frame, cor):
        conteudo = tk.Label(frame,
                            text="Módulo de Fitopatologia\n\n"
                                 "• Diagnóstico de doenças\n"
                                 "• Identificação de fungos\n"
                                 "• Análise de bactérias\n"
                                 "• Controle fitossanitário",
                            font=('Arial', 12),
                            bg=cor,
                            fg='white',
                            justify='left')
        conteudo.pack(pady=20)

    def criar_conteudo_entomologia(self, frame, cor):
        conteudo = tk.Label(frame,
                            text="Módulo de Entomologia\n\n"
                                 "• Identificação de insetos\n"
                                 "• Controle de pragas\n"
                                 "• Monitoramento populacional\n"
                                 "• Manejo integrado",
                            font=('Arial', 12),
                            bg=cor,
                            fg='white',
                            justify='left')
        conteudo.pack(pady=20)

    def criar_conteudo_cadastros(self, frame, cor):
        # Frame para formulário de cadastro
        form_frame = tk.Frame(frame, bg=cor)
        form_frame.pack(pady=20)

        # Campos do formulário
        campos = [
            ("Nome:", 0),
            ("Email:", 1),
            ("Telefone:", 2),
            ("Setor:", 3)
        ]

        entries = []
        for texto, linha in campos:
            lbl = tk.Label(form_frame, text=texto, bg=cor, fg='white', font=('Arial', 10))
            lbl.grid(row=linha, column=0, sticky='w', pady=5, padx=5)

            entry = tk.Entry(form_frame, width=30, font=('Arial', 10))
            entry.grid(row=linha, column=1, pady=5, padx=5)
            entries.append(entry)

        self.entries_cadastro = entries

        # Botão Cadastrar
        btn_cadastrar = tk.Button(form_frame,
                                  text="CADASTRAR",
                                  bg='#2c3e50',
                                  fg='white',
                                  font=('Arial', 10, 'bold'),
                                  command=self.cadastrar_usuario)
        btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=15)

    def cadastrar_usuario(self):
        dados = [entry.get() for entry in self.entries_cadastro]
        if all(dados):
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            for entry in self.entries_cadastro:
                entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")


def main():
    root = tk.Tk()
    app = SistemaPrincipal(root)

    # Centralizar a janela principal
    root.eval('tk::PlaceWindow . center')

    root.mainloop()


if __name__ == "__main__":
    main()