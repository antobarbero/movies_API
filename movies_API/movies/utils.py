from collections import OrderedDict


def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_number(number):
        for r in roman.keys():
            x, y = divmod(number, r)
            yield roman[r] * x
            number -= (r * x)
            if number > 0:
                roman_number(number)
            else:
                break

    return "".join([a for a in roman_number(num)])
