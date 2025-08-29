#produtos =[{nome:"arroz", qtd:2, valor:23.00}]
#pessoas =[{nome:"luiz"},{nome:"miguel"}]


#lendo o arquivo
import json

inventario = []
try :
    with open ('loja.json','r') as arquivo:
        inventario= json.load(arquivo)
        print("arquivo carregado!")
except FileNotFoundError:
    print("arquivo não encontrado")

print("\n----cadastrar produto----")

nome_produto= input("digite o nome do produto:")
while True:
    try:
        quantidade= int(input("digite a quantidade:"))
        break;
    except ValueError:
        print("digite apenas numero")
while True:
    try:
        preco = float(input("digite o preço:"))   
        break;
    except ValueError:
        print("digite o preço corretamente")

novo_produto= {
    "nome_produto": nome_produto,
    "quantidade": quantidade, 
    "preco": preco, 
    "tem_estoque": quantidade > 0 }

#escrever no arquivo json

inventario.append(novo_produto)
with open('loja.json','w')as arquivo :
    json.dump(inventario,arquivo,indent=4)
    print(f"\n produto {nome_produto} foi cadastrado")
