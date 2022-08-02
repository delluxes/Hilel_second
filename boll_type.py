a: int = 3 != 5
print(a)

b = 5 >= 5
c = 5 <= 5
d = 5 == 5
print(b, c, d,)

operanta = (True and True) or False
operanta1 = (True or not False) or True
operanta2 = (not not not False and True) and True
operanta3 = True or True and not False
operanta4 = True and True and True
print(operanta, operanta1, operanta2, operanta3, operanta4)

op = None != 7 or None == 7
op2 = type(op)
print(op)
op1 = '' == (10 - 1) or '' != (10-1)
print(op1)
