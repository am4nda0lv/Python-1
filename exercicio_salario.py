# Solicita o salário atual e o percentual de aumento.
salario = float(input("Digite seu salário: "))
percentual = float(input("Digite o percentual de aumento: "))

# Calcula o salário após o aumento.
novo_salario = salario * (1 + percentual / 100)

# Exibe o salário atual, o percentual e o novo salário.
print(
    f"O meu salário é R${salario:.2f}, o percentual de aumento foi "
    f"{percentual:.1f}% e o novo salário será de R${novo_salario:.2f}"
)