#3
for i in range(10, 0, -1):
    print (i)

#4

numero = int(input("digite um numero para ver a tabuada:"))

for i in range (1, 11):
    print(f"{numero} x {i} = {numero * i}")

#5 
    
    soma = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero

print(f"A soma total é: {soma}")

#6
numero_secreto = 5

while True:
    palpite = int(input("Tente adivinhar o número secreto: "))
    
    if palpite < numero_secreto:
        print("Muito baixo.")
    elif palpite > numero_secreto:
        print("Muito alto.")
    else:
        print("Parabéns, você acertou!")
        break

#lista_mercado = ["maçã", "banana", "leite"]

print("Lista de mercado atual:", lista_mercado)

novo_item = input("Digite um item para adicionar à lista: ")

lista_mercado.append(novo_item)

print("Lista de mercado atualizada:", lista_mercado)



