entery = input('Enter your any text: ')
inputed = entery

cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
       'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in inputed:
    if i in cap:
        print(i)

spacebar = ' '
for index, letter in enumerate(inputed):
    if letter == spacebar:
        print(f'spacebar has {index} index')
    else:
        pass

alfabet = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
for i in inputed:
    if i in alfabet:
        print(i)
num = " "

for i in inputed:
    if i.isdigit():
        num = num + i
    if len(num) >= 3:
        print('You have entered 3 numbers in line, script closed')
        break
else:
    print('The script worked correctly')
