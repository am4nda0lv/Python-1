# Reescreve o cálculo de aumento salarial usando match/case.
salario = float(input("Digite seu salário: R$"))
cargo = input("Digite o nível do cargo: ").strip().lower()

match cargo:
    case "junior":
        novo_salario = salario * 1.1
    case "pleno":
        novo_salario = salario * 1.2
    case "senior":
        novo_salario = salario * 1.3
    case _:
        print("Cargo não identificado!")
        novo_salario = None

if novo_salario is not None:
    print(
        f"O meu salário é R${salario:.2f}, mas com o meu cargo {cargo}, "
        f"o novo salário será de R${novo_salario:.2f}"
    )