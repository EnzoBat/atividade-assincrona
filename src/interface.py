import tkinter as tk
from tkinter import ttk, messagebox
from crud import create_aluno, read_alunos, update_aluno, delete_aluno
from aluno import Aluno

def criar_janela_principal():
    janela = tk.Tk()
    janela.title("Sistema de Cadastro de Alunos - TechEduca")
    janela.geometry("700x500")
    janela.configure(bg="#f0f0f0")

    # --- Campos ---
    tk.Label(janela, text="Nome do Aluno:", bg="#f0f0f0").pack()
    entrada_nome = tk.Entry(janela, width=50)
    entrada_nome.pack(pady=5)

    tk.Label(janela, text="CPF:", bg="#f0f0f0").pack()
    entrada_cpf = tk.Entry(janela, width=50)
    entrada_cpf.pack(pady=5)

    tk.Label(janela, text="Data de Nascimento (YYYY-MM-DD):", bg="#f0f0f0").pack()
    entrada_data = tk.Entry(janela, width=50)
    entrada_data.pack(pady=5)

    tk.Label(janela, text="Status (ativo/inativo):", bg="#f0f0f0").pack()
    entrada_status = tk.Entry(janela, width=50)
    entrada_status.pack(pady=5)

    # --- BARRA DE RELATÓRIOS (FILTROS) ---
    barra = tk.Frame(janela, bg="#f0f0f0")
    barra.pack(pady=5, fill="x")

    tk.Label(barra, text="Buscar por nome:", bg="#f0f0f0").pack(side="left", padx=(0,6))
    entrada_busca_nome = tk.Entry(barra, width=30)
    entrada_busca_nome.pack(side="left")

    var_somente_ativos = tk.BooleanVar()
    ck_ativos = tk.Checkbutton(barra, text="Somente Ativos", bg="#f0f0f0", variable=var_somente_ativos)
    ck_ativos.pack(side="left", padx=10)

    tk.Button(barra, text="Buscar", command=lambda: carregar_relatorio()).pack(side="left", padx=5)
    tk.Button(barra, text="Limpar Filtros", command=lambda: limpar_filtros()).pack(side="left", padx=5)
    tk.Button(barra, text="Atualizar", command=lambda: carregar_relatorio()).pack(side="left", padx=5)

    # --- Funções ---
    def limpar_campos():
        entrada_nome.delete(0, tk.END)
        entrada_cpf.delete(0, tk.END)
        entrada_data.delete(0, tk.END)
        entrada_status.delete(0, tk.END)

    def carregar_lista():
        for item in tabela.get_children():
            tabela.delete(item)
        try:
            alunos = read_alunos()
            for a in alunos:
                tabela.insert("", "end", values=(a[0], a[1], a[2], a[3], a[4]))
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar lista: {e}")

    def aplicar_filtros(alunos, nome_busca, somente_ativos):
        # alunos: lista de tuplas (id, nome, cpf, data_nascimento, status)
        if nome_busca:
            nb = nome_busca.strip().lower()
            alunos = [a for a in alunos if nb in (a[1] or "").lower()]
        if somente_ativos:
            alunos = [a for a in alunos if (a[4] or "").strip().lower() == "ativo"]
        return alunos

    def carregar_relatorio():
        # Limpa a tabela e carrega com base nos filtros
        for item in tabela.get_children():
            tabela.delete(item)
        try:
            dados = read_alunos()
            dados = aplicar_filtros(dados, entrada_busca_nome.get(), var_somente_ativos.get())
            if not dados:
                messagebox.showinfo("Relatório", "Nenhum registro encontrado para os filtros informados.")
            for a in dados:
                tabela.insert("", "end", values=(a[0], a[1], a[2], a[3], a[4]))
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao gerar relatório: {e}")

    def limpar_filtros():
        entrada_busca_nome.delete(0, tk.END)
        var_somente_ativos.set(False)
        carregar_relatorio()

    def cadastrar():
        nome = entrada_nome.get().strip()
        cpf = entrada_cpf.get().strip()
        data = entrada_data.get().strip()
        status = entrada_status.get().strip().lower()

        if not (nome and cpf and data and status):
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return
        if status not in ['ativo', 'inativo']:
            messagebox.showerror("Erro", "Status deve ser 'ativo' ou 'inativo'.")
            return

        try:
            aluno = Aluno(nome=nome, cpf=cpf, data_nascimento=data, status=status)
            create_aluno(aluno)
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
            limpar_campos()
            carregar_relatorio()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

    def atualizar():
        selected = tabela.selection()
        if not selected:
            messagebox.showerror("Erro", "Selecione um aluno na lista para atualizar.")
            return
        aluno_id = tabela.item(selected[0])['values'][0]

        novo_status = entrada_status.get().strip().lower()
        if novo_status not in ['ativo', 'inativo']:
            messagebox.showerror("Erro", "Status deve ser 'ativo' ou 'inativo'.")
            return

        try:
            sucesso = update_aluno(aluno_id, {"status": novo_status})
            if sucesso:
                messagebox.showinfo("Sucesso", "Status atualizado com sucesso!")
                carregar_relatorio()
            else:
                messagebox.showwarning("Aviso", "Nenhum registro foi atualizado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível atualizar: {e}")

    def excluir():
        selected = tabela.selection()
        if not selected:
            messagebox.showerror("Erro", "Selecione um aluno na lista para excluir.")
            return
        aluno_id = tabela.item(selected[0])['values'][0]

        try:
            sucesso = delete_aluno(aluno_id)
            if sucesso:
                messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")
                limpar_campos()
                carregar_relatorio()
            else:
                messagebox.showwarning("Aviso", "Nenhum registro foi excluído.")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível excluir: {e}")

    def on_selecionar(event):
        selected = tabela.selection()
        if not selected:
            return
        valores = tabela.item(selected[0])['values']
        entrada_nome.delete(0, tk.END)
        entrada_nome.insert(0, valores[1])
        entrada_cpf.delete(0, tk.END)
        entrada_cpf.insert(0, valores[2])
        entrada_data.delete(0, tk.END)
        entrada_data.insert(0, valores[3])
        entrada_status.delete(0, tk.END)
        entrada_status.insert(0, valores[4])

    # --- Botões ---
    frame_botoes = tk.Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=10)

    tk.Button(frame_botoes, text="Cadastrar", width=15, bg="#4CAF50", fg="white", command=cadastrar).grid(row=0, column=0, padx=5)
    tk.Button(frame_botoes, text="Atualizar", width=15, bg="#2196F3", fg="white", command=atualizar).grid(row=0, column=1, padx=5)
    tk.Button(frame_botoes, text="Excluir", width=15, bg="#f44336", fg="white", command=excluir).grid(row=0, column=2, padx=5)
    tk.Button(frame_botoes, text="Consultar", width=15, bg="#9C27B0", fg="white", command=carregar_relatorio).grid(row=0, column=3, padx=5)

    # --- Treeview ---
    colunas = ("id", "nome", "cpf", "data_nascimento", "status")
    tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=10)
    for c in colunas:
        tabela.heading(c, text=c.title())

    tabela.column("id", width=60, anchor="center")
    tabela.column("nome", width=200, anchor="w")
    tabela.column("cpf", width=140, anchor="center")
    tabela.column("data_nascimento", width=120, anchor="center")
    tabela.column("status", width=100, anchor="center")

    tabela.pack(pady=10, fill="both", expand=True)
    tabela.bind("<<TreeviewSelect>>", on_selecionar)

    carregar_relatorio()
    janela.mainloop()
