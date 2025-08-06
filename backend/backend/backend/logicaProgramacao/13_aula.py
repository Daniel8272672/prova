nota =int(input("digite sua nota:"))
match nota:
    case 10:
        print("parabens nota maxima")
    case 7|8|9:
        print("ta na media")
    case 0|1|2|3|4|5|6:
        print("reprovado")
    case _:
        print("nota invalida")
