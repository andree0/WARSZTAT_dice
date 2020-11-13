from random import randint


def throw_dice(kind_of_throw):
    throw = 0
    type_of_dices = [3, 4, 6, 8, 10, 12, 20, 100]  # ilość ścian kostek, które występują w grach
    if "D" in kind_of_throw:
        kind_of_throw = kind_of_throw.split("D")
        x = kind_of_throw[0]

        if "+" in kind_of_throw[1]:
            kind_of_throw[1] = kind_of_throw[1].split("+")
            y = kind_of_throw[1][0]
            z = kind_of_throw[1][1]
            try:
                y = int(y)
                z = int(z)
            except ValueError:
                return "Podałeś zły parametr"

            if y not in type_of_dices:
                return "W żadnej grze nie stosuje się takiej kostki"
            else:
                throw += z

        elif "-" in kind_of_throw[1]:
            kind_of_throw[1] = kind_of_throw[1].split("-")
            y = kind_of_throw[1][0]
            z = kind_of_throw[1][1]
            try:
                y = int(y)
                z = int(z)
            except ValueError:
                return "Podałeś zły parametr"

            if y not in type_of_dices:
                return "W żadnej grze nie stosuje się takiej kostki"
            else:
                throw -= z

        else:
            y = kind_of_throw[1]
            try:
                y = int(y)
            except ValueError:
                return "Podałeś zły parametr"

        if len(x) == 0:
            x = 1
        else:
            try:
                x = int(x)
            except ValueError:
                return "Podałeś zły parametr"

        for i in range(x):
            throw += randint(1, y + 1)

        return throw

    else:
        return "Podałeś zły parametr."


# przykłady do sprawdzenia
# 2D10+10
# D6
# D6-2
# 2D10
# 2D99-5
# dupa
# LLKD6+10
# 2Doko+10
# 2D10+gygy
# ghgDghg+10
# ghgD6+ldcld
# 3Djkkj-jhjh
# 3Dhjhj
# Dhjhj

kind_of_throw = "ghgD6+ldcld"
print(throw_dice(kind_of_throw))
