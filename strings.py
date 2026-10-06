# Exemplos de formatação de strings; todos exibem nome, idade e valor com duas casas decimais.

print("%s tem %d anos e R$%.2f" % ("João", 40, 50.453))

print("{} tem {} anos e R${:.2f}".format("João", 40, 50.453))
nome, idade, dinheiro = "João", 40, 50.453

print(f"{nome} tem {idade} anos e R${dinheiro:.2f}")
