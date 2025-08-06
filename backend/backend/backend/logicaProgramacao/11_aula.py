num1 = int(input("digite um numero:"))
num2 = int(input ("digite um numero:"))
operaçao = (input ("digite a operaçao : (+,-,*,/):"))
match operaçao:
    case "+":
        soma = num1+num2
        print("soma",soma)

    case "/":
        divisao = num1/num2
        print("divisao",divisao)

    case "-":
        subtraçao = num1-num2
        print("subtraçao",subtraçao)

    case "*":
        multiplicaçao = num1*num2
        print("multiplicaçao",multiplicaçao)