a = 2
b = 5
c = 10
calculation: int = 10 - 5
sym = 'Hello world'
d = calculation
summerry = c + d
e = 20 / 5
text: str = sym
message = 'Command said you: ' + sym
print(a, "| his type:", type(a))
print(b, "| his type:", type(b))
print(c, "| his type:", type(c))
print(calculation, "| his type:", type(calculation))
print(sym, "| his type:", type(sym))
print(d, "| his type:", type(d))
print(summerry, "| his type:", type(summerry))
print(e, "| his type:", type(e))
print(text, "| his type:", type(text))
print(message, "| his type:", type(message))

print('###################################################################################')

print(a, type(a) , b , type(b) , c , type(c) ,              #print all items using only one print
      calculation , type(calculation) , sym , type(sym) , "\n" ,
      d, type(d) , summerry , type(summerry) , e , type(e) ,
      text , type(text) , message , type(message) )