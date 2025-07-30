#7
    
lista_mercado = ["maçã", "banana", "leite"]

print("Lista de mercado atual:", lista_mercado)

novo_item = input("Digite um item para adicionar à lista: ")

lista_mercado.append(novo_item)

print("Lista de mercado atualizada:", lista_mercado)

#8 
numeros = [10, 5, 20, 8, 15]
maior = numeros[0]

for num in numeros:
    if num > maior:
        maior = num

print(f"O maior número da lista é: {maior}")