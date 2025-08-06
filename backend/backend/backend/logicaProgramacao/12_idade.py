idade = int(input("digite sua idade"))

match idade:
    case x if x < 12:
        fasedavida = "criança"
        print("sua fase da vida é", fasedavida)

    case x if x >=12 and x < 18:
        fasedavida= "adolecente"
        print("sua fase da vida é:", fasedavida)

    case x if x >= 18 and x < 60:
        fasedavida= "idoso"
        print("sua fase da vida é:", fasedavida)

    case x if x >=100:
        fasedavida= "mumia"
        print("sua fase da vida é:", fasedavida)

