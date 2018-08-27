# Numbers in French
numbers_vignt = {'0': 'zero', '1': 'un', '2': 'deux', '3': 'trois', '4': 'quatre', '5': 'cinq', '6': 'six', '7': 'sept',
'8': 'huit', '9': 'neuf', '10': 'dix', '11': 'onze', '12': 'douze', '13': "treize", '14': 'quatorze', '15': 'quinze',
'16': 'seize', '17': 'dix-sept', '18': 'dix-huit', '19': 'dix-neuf', '20': 'vingt'}
numbers_tens = {'10': 'dix', '20': 'vingt', '30': 'trente', '40': 'quarante', '50': 'cinquante', '60': 'soixante', '70': 'soixante-dix',
'80': 'quatre-vingt', '90': 'quatre-vingt-dix', '100': 'cent', '1000': 'mille'}

while True:
    print('Enter a number \nor type \'done\' to finish the program: ')
    dima = input()
    
    if dima == 'done':
        print("Learn French! Good Luck, Dima")
        quit()

    try:
        int(dima)
    except:
        print('Enter a valid integer number!\n')
        continue

    if int(dima) > 100:
        print("Enter a number less than 100 \n\n P.S.: Developer is a lazy piece of shit\n")
        continue
    if int(dima) < 0:
        print("Use positive integers only! \n\n P.S.: Developer is a lazy piece of shit\n")
        continue

    digits = []
    for i in dima:
        digits.append(i)

    if int(dima) < 20:
        print(str(dima),"-",numbers_vignt[str(dima)])
    elif int(digits[1]) == 0:
        print(str(dima),"-",numbers_tens[str(dima)])
    elif int(digits[0]) == 7:
        if int(digits[1]) in [*range(1,7)]:
            print(str(dima),'-',numbers_tens['60']+'-'+numbers_vignt['1'+str(digits[1])])
        else:
            print(str(dima),'-',numbers_tens['70']+'-'+numbers_vignt[str(digits[1])])
    elif int(digits[0]) == 9:
        if int(digits[1]) in [*range(1,7)]:
            print(str(dima),'-',numbers_tens['80']+'-'+numbers_vignt['1'+str(digits[1])])
        else:
            print(str(dima),'-',numbers_tens['90']+'-'+numbers_vignt[str(digits[1])])
    else:
        print(str(dima),'-',numbers_tens[digits[0]+"0"]+'-'+numbers_vignt[str(digits[1])])
        




