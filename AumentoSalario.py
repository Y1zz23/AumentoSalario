salario = int(input("Digite o valor do salário? R$"))
if salario > 1250:
    print("Seu salario antes do ajuste {}".format(salario))
    aumento = salario * 0.10
    salario = salario + aumento
    print("Após o ajuste de 10% voce irá receber {}".format(salario))
else:
    print("Seu salario antes do ajuste {}".format(salario))
    aumento = salario * 0.15
    salario = salario + aumento
    print("Após o ajuste de 15% voce irá receber {}".format(salario))
    
#Outro Jeito
if salario <=1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + ( salario * 10 /100)
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salario.novo))