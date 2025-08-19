# Sistema bancário com criação de conta

usuarios = {}  # Armazenar os usuários: login -> dados (nome, cpf, senha)
contas = {}    # Armazenar os dados bancários: login -> saldo, extrato, etc.
usuario_logado = None

menu_principal = """
[C] Criar conta
[L] Login
[Q] Sair

=> """

menu_banco = """
[d] Depositar
[s] Sacar
[e] Extrato
[l] Logout

=> """

LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500

while True:
    if not usuario_logado:
        opcao = input(menu_principal).lower()

        if opcao == "c":
            print("\n== CRIAÇÃO DE CONTA ==")
            nome = input("Nome completo: ")
            cpf = input("CPF (somente números): ")
            login = input("Crie um login: ")
            senha = input("Crie uma senha: ")

            if login in usuarios:
                print("Esse login já está em uso. Tente outro.")
            else:
                usuarios[login] = {"nome": nome, "cpf": cpf, "senha": senha}
                contas[login] = {"saldo": 0, "extrato": "", "saques": 0}
                print("Conta criada com sucesso!")

        elif opcao == "l":
            print("\n== LOGIN ==")
            login = input("Login: ")
            senha = input("Senha: ")

            if login in usuarios and usuarios[login]["senha"] == senha:
                usuario_logado = login
                print(f"\nBem-vindo(a), {usuarios[login]['nome']}!")
            else:
                print("Login ou senha incorretos.")

        elif opcao == "q":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida.")
    
    else:
        # Usuário logado, pode acessar o banco
        opcao = input(menu_banco).lower()
        conta = contas[usuario_logado]

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                conta["saldo"] += valor
                conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso.")
            else:
                print("Valor inválido para depósito.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            if valor <= 0:
                print("Valor inválido.")
            elif valor > conta["saldo"]:
                print("Saldo insuficiente.")
            elif valor > LIMITE_SAQUE_VALOR:
                print("Saque excede o limite por operação (R$ 500).")
            elif conta["saques"] >= LIMITE_SAQUES:
                print("Limite diário de saques excedido.")
            else:
                conta["saldo"] -= valor
                conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
                conta["saques"] += 1
                print("Saque realizado com sucesso.")

        elif opcao == "e":
            print("\n========== EXTRATO ==========")
            print("Sem movimentações." if not conta["extrato"] else conta["extrato"])
            print(f"Saldo atual: R$ {conta['saldo']:.2f}")
            print("==============================")

        elif opcao == "l":
            print(f"Logout de {usuarios[usuario_logado]['nome']}")
            usuario_logado = None

        else:
            print("Desculpa, Opção inválida.")
