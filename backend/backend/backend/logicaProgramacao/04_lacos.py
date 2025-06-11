# for


for i in range(5):
    print("contando:", i)
#while
    


for i in range(11):
    print("contando:", i)




#terceiro
    
senha = ""
while senha != "danizin":
    senha = input("Digite a senha: ")
    print("senha incorreta.")

print("Acesso liberado.")
#quarto

numeros = (10, 15, 22, 33, 42, 55, 60, 73, 88, 91, 100)

quantidade_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        quantidade_pares += 1

print(f"Quantidade de números pares: {quantidade_pares}")
# quinto 

soma = 0
valor = 1

while valor != 0:
    valor = int(input("Digite um valor:"))
    soma + valor

print("ta ai a soma")