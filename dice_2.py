import re
from random import randint as r

POSSIBLE_DICES = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
CODE = r'^(\d*)D(\d+)([+|-]\d+)*$'


def roll_the_dice(dice_code):
    check_code = re.search(CODE, dice_code)
    if check_code:
        try:
            multiply = int(check_code.group(1))
        except ValueError:
            multiply = 1

        dice = int(check_code.group(2))
        try:
            modifier = int(check_code.group(3))
        except (ValueError,TypeError):
            modifier = 0

        result = 0
        for i in range(multiply):
            result += r(1, dice)

        result += modifier
        return result
    else:
        return "Wrong input"


if __name__ == '__main__':
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))
    print(roll_the_dice("throw 2D6+15"))
