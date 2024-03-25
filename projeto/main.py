from funcoes import Funcoes

def cadastrar_veiculo():
    placa = input("Digite a placa do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    motorista = input("Digite o nome do motorista do veículo: ")
    veiculo = {"placa": placa, "modelo": modelo, "motorista": motorista}
    funcoes.cadastrar_veiculo(veiculo)
    print("Veículo cadastrado com sucesso!")

def listar_veiculos():
    funcoes.relatorio_todos_veiculos()

def cadastrar_motorista():
    nome = input("Digite o nome do motorista: ")
    funcoes.cadastrar_motorista(nome)
    print("Motorista cadastrado com sucesso!")

def listar_motoristas():
    funcoes.relatorio_todos_motoristas()

def veiculos_do_motorista():
    motorista = input("Digite o nome do motorista: ")
    funcoes.relatorio_veiculos_do_motorista(motorista)

def main():
    global funcoes
    funcoes = Funcoes()

    while True:
        print("\n===== Menu Principal =====")
        print("1. Cadastrar Veículo")
        print("2. Listar Veículos")
        print("3. Cadastrar Motorista")
        print("4. Listar Motoristas")
        print("5. Veículos do Motorista")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_veiculo()
        elif opcao == "2":
            listar_veiculos()
        elif opcao == "3":
            cadastrar_motorista()
        elif opcao == "4":
            listar_motoristas()
        elif opcao == "5":
            veiculos_do_motorista()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()