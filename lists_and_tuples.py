entery = input('Write your text here: ')
inputed = entery.split(' ')
print(f'{inputed[2::3]}')

input_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
output_list = [1, 2.1, -1, '6', 9, '3', 18, -1]

generation = [i if type(i) == float else i
             if (type(i) == int and i % 2 == 0) else i ** 2
             if (type(i) == int and i % 2 != 2) else (str(int(i) * 3))
             if (type(i) == str and i.isdigit()) else -1
             for i in input_list]

print(generation)
