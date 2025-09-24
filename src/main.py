from aluno import Aluno
from crud import create_aluno, read_aluno_by_id, read_alunos, update_aluno, delete_aluno

def main():
    print("=== TESTANDO CRUD ===")

    # CREATE
    aluno1 = Aluno(nome="João", cpf="12345678900", data_nascimento="2005-05-10", status="ativo")
    novo_id = create_aluno(aluno1)
    print("Novo aluno criado com ID:", novo_id)

    # READ por ID
    print("Buscando aluno criado...")
    print(read_aluno_by_id(novo_id))

    # READ lista
    print("Listando todos os alunos:")
    print(read_alunos())

    # UPDATE
    print("Atualizando status do aluno...")
    update_aluno(novo_id, {"status": "inativo"})
    print(read_aluno_by_id(novo_id))

    # DELETE
    print("Removendo aluno...")
    delete_aluno(novo_id)
    print(read_aluno_by_id(novo_id))  # Deve retornar None

if __name__ == "__main__":
    main()
