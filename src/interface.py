import tkinter as tk
from tkinter import messagebox
from aluno import Aluno
from crud import create_aluno

# Cores e estilos
BG_COLOR = "#f0f4f8"
ENTRY_BG = "#ffffff"
BTN_COLOR = "#4caf50"
BTN_TEXT = "#ffffff"
FONT_LABEL = ("Segoe UI", 10)
FONT_TITLE = ("Segoe UI", 14, "bold")


def cadastrar_aluno(nome, cpf, data_nascimento):
    if not nome or not cpf or not data_nascimento:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos.")
        return

    aluno = Aluno(nome=nome, cpf=cpf, data_nascimento=data_nascimento)
    try:
        novo_id = create_aluno(aluno)
        messagebox.showinfo("Sucesso", f"Aluno cadastrado com sucesso! ID: {novo_id}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar aluno:\n{str(e)}")


def criar_interface():
    janela = tk.Tk()
    janela.title("Cadastro de Alunos - TechEduca")
    janela.geometry("420x300")
    janela.configure(bg=BG_COLOR)
    janela.resizable(False, False)

    frame = tk.Frame(janela, bg=BG_COLOR, padx=20, pady=20)
    frame.pack(expand=True)

    # Título
    lbl_titulo = tk.Label(frame, text="Cadastro de Aluno", font=FONT_TITLE, bg=BG_COLOR, fg="#333")
    lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Nome
    lbl_nome = tk.Label(frame, text="Nome:", bg=BG_COLOR, font=FONT_LABEL)
    lbl_nome.grid(row=1, column=0, sticky="e", pady=5)
    entry_nome = tk.Entry(frame, width=30, bg=ENTRY_BG)
    entry_nome.grid(row=1, column=1, pady=5)

    # CPF
    lbl_cpf = tk.Label(frame, text="CPF:", bg=BG_COLOR, font=FONT_LABEL)
    lbl_cpf.grid(row=2, column=0, sticky="e", pady=5)
    entry_cpf = tk.Entry(frame, width=30, bg=ENTRY_BG)
    entry_cpf.grid(row=2, column=1, pady=5)

    # Data de nascimento
    lbl_data = tk.Label(frame, text="Data de Nascimento:", bg=BG_COLOR, font=FONT_LABEL)
    lbl_data.grid(row=3, column=0, sticky="e", pady=5)
    entry_data = tk.Entry(frame, width=30, bg=ENTRY_BG)
    entry_data.grid(row=3, column=1, pady=5)

    # Botão cadastrar
    btn_cadastrar = tk.Button(
        frame,
        text="Cadastrar Aluno",
        bg=BTN_COLOR,
        fg=BTN_TEXT,
        width=25,
        height=1,
        font=("Segoe UI", 10, "bold"),
        command=lambda: cadastrar_aluno(entry_nome.get(), entry_cpf.get(), entry_data.get())
    )
    btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=20)

    janela.mainloop()
