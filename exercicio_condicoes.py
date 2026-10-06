# Lê o salário atual e normaliza o cargo para aceitar maiúsculas/minúsculas
# e espaços extras digitados pelo usuário.
salario = float(input("Digite seu salário: R$"))
cargo = input("Digite o nível do cargo (junior, pleno ou senior): ").strip().lower()

# Aplica o percentual de aumento correspondente ao nível do cargo.
if cargo == "junior":
    novo_salario = salario * 1.10
elif cargo == "pleno":
    novo_salario = salario * 1.20
elif cargo == "senior":
    novo_salario = salario * 1.30
else:
    print("Cargo não identificado!")
    raise SystemExit(1)

# Exibe o salário atual, o cargo e o novo salário.
print(
    f"O salário atual é R${salario:.2f}; cargo: {cargo}; "
    f"novo salário: R${novo_salario:.2f}."
)