import json

selecao = []

try :
    with open ('usuarios.json','r') as arquivo:
        selecao= json.load(arquivo)
        print("arquivo carregado!")
except FileNotFoundError:
    print("arquivo não encontrado")

print("\n----cadastrar usuario----")

nome_usuario= input("cadastre seu nome:")
while True:
    try:
        telefone= int(input("digite o numero de telefone:"))
        break;
    except ValueError:
        print("digite apenas numeros")

while True:
    try:
        cidade= input("digite sua cidade:")
        break;
    except ValueError:
        print("cidade invalida")
while True:
    try:
        idade=int(input("digite sua idade:"))
        break;
    except ValueError:
        print("digite apenas numeros")
while True:
    try:
        sexo=input("digite seu genero")
        break;
    except TypeError:
        print("tem algo errado")

novo_usuario= {
    "novo_usuario": nome_usuario,
    "telefone": telefone, 
    "cidade": cidade, 
    "idade": idade,
    "sexo": idade,}

selecao.append(novo_usuario)
with open('usuarios.json','w')as arquivo :
    json.dump(selecao,arquivo,indent=5)
    print(f"\n usuario {nome_usuario} foi cadastrado")



