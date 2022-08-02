first_name = input('Write your name here:')
name = first_name.strip()

print('Hello, dear:', name.capitalize())
print(f'Your name has:{len(name)} symbols' )
print(name.capitalize()[::-1])
