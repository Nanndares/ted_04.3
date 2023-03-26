## Exercício 1

numero=int(input("Insira o seu número: "))
if numero >= 0:
        print("este número é positivo.")
else:
        print("este número é negativo.")

## Exercício 3

valor1=(1.30)
valor2=(1.00)

quantidade=int(input("Quantas maças foram compradas?"))

if quantidade < 12:
	print('Valor total R$',(valor1 * quantidade))
else:
	print('Valor total R$',(valor2 * quantidade))