new_dict = {element: chr(element) for element in range(0, 256)}
print(new_dict)

try:
    user_text = input('Enter anythink you want: ')
    while user_text.isalpha():
        break
    else:
        print('You cant use numbers or spacebar in input field!')
        sys.exit()
    password = int(input("Enter your pass(can't use letters)"))
    new_list = []
    letters = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,'f': 6, 'g': 7,
        'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
        'o': 15,'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,'u': 21,
        'v': 22, 'w': 23, 'x': 24, 'y': 25,'z': 26
    }
    for letter in user_text:
        if letter in letters:
            new_index = letters[letter] + password
            new_list.append(list(letters.keys())[list(letters.values()).index(new_index)])
    print(''.join(new_list))
except (ValueError, NameError):
    print('Somethint went wrong. Script was ended!')
