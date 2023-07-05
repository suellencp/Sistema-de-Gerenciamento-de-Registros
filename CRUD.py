# Lista para armazenar os registros
registros = []

def criar_registro():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    registro = {"nome": nome, "idade": idade}
    registros.append(registro)
    print("Registro criado com sucesso!")

def listar_registros():
    if len(registros) == 0:
        print("Nenhum registro encontrado.")
    else:
        for i, registro in enumerate(registros):
            print(f"Registro {i+1}:")
            print(f"Nome: {registro['nome']}")
            print(f"Idade: {registro['idade']}")
            print()

def atualizar_registro():
    listar_registros()
    if len(registros) == 0:
        return
    indice = int(input("Digite o número do registro que deseja atualizar: ")) - 1
    if indice < 0 or indice >= len(registros):
        print("Índice inválido.")
        return
    registro = registros[indice]
    nome = input("Digite o novo nome: ")
    idade = input("Digite a nova idade: ")
    registro["nome"] = nome
    registro["idade"] = idade
    print("Registro atualizado com sucesso!")

def excluir_registro():
    listar_registros()
    if len(registros) == 0:
        return
    indice = int(input("Digite o número do registro que deseja excluir: ")) - 1
    if indice < 0 or indice >= len(registros):
        print("Índice inválido.")
        return
    registro = registros.pop(indice)
    print("Registro excluído com sucesso!")

# Função principal para interação com o usuário
def main():
    while True:
        print("Selecione uma opção:")
        print("1. Criar registro")
        print("2. Listar registros")
        print("3. Atualizar registro")
        print("4. Excluir registro")
        print("5. Sair")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == "1":
            criar_registro()
        elif opcao == "2":
            listar_registros()
        elif opcao == "3":
            atualizar_registro()
        elif opcao == "4":
            excluir_registro()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    main()