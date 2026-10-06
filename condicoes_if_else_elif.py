# As condições permitem executar diferentes blocos de código conforme o caso.

# if executa o bloco quando a condição é verdadeira.
idade = 20
if idade >= 18:
    print("Maior de idade")

# else executa o bloco alternativo quando a condição do if é falsa.
idade = 16
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# elif verifica outra condição quando as condições anteriores são falsas.
nota = 7
if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")