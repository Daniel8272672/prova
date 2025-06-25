def contar_ate_dez():

  for i in range(1, 11):
    print(i)


contar_ate_dez()

#2

def repetir_nome(nome, numero):

  print("Exercício 2: Repetir Nome")
  for _ in range(numero): 
    print(nome)

repetir_nome("Alice", 3)
repetir_nome("Python", 5)
print("-" * 30)

#3 
def somar_numeros_usuario():
  soma = 0
  for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero
  print(f"A soma: {soma}")

somar_numeros_usuario()
#4 
def tabuada(numero):
  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

tabuada(7)
tabuada(9)

#5

def numeros_pares_ate_vinte():
  for i in range(1, 21):
    if i % 2 == 0:
      print(i)

numeros_pares_ate_vinte()

