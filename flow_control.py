while True:
    first_num = (input('First symbol:'))
    if first_num == 'exit':
        print('Closed')
        break
    first_num = float(first_num) if first_num.find(".") != -1 else int(first_num)
    second_num = (input('Second symbol:'))
    if second_num == 'exit':
        print('Closed')
        break
    second_num = float(second_num) if second_num.find(".") != -1 else int(second_num)
    operation = input('Choose your item(+,-,/,*):')

    if operation not in ('+', '-', '/', '*'):
        print('Only Symbols')
        continue
    if operation == '+':
        print(first_num + second_num)
    elif operation == '-':
        print(first_num - second_num)
    elif operation == '/':
        print(first_num / second_num)
    elif operation == '*':
        print(first_num * second_num)
