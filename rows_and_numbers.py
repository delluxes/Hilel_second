username = input("Please write your name: ")
result_name = f"Hello {username} ! "
print(result_name)
item_input = input('Write your number(like: 5.1):')
result_item: int = int(float(item_input))
exponentiation: int = result_item ** 4
exponentiation1 = result_item ** 0.5
exponentiation2: int = result_item % 2
print(f'Your number: {item_input}')
print(f'Your integer: {result_item}')
print(f'Your 4th degree from number: {exponentiation}')
print(f'Your square root: {exponentiation1}')
print(f'Your remainder of the division: {exponentiation2}')