first_input = input('Enter your first text: ')
second_input = input('Enter your second text: ')

first_setup = {x for x in first_input if x.isalpha()}
second_setup = {x for x in second_input if x.isalpha()}

print(f'In the text there are such letters: {first_setup & second_setup}')

###########################################################

first_set = {x for x in first_input if x.isdigit()}
first_set2 = {x for x in second_input if x.isdigit()}

len_numbers_1 = first_set - first_set2
len_numbers_2 = first_set2 - first_set
lene = len_numbers_1 & len_numbers_2

print(f'Your text: {lene}')
############################################
a_set = {1, 3432, 234, 123, 456}
b_set = {'asdasd', 456, 7, 2, 1}
c_set = {2, 45, 'asdasdasdsa'}

a_set.update(b_set, c_set)
print(a_set)
############################################
q_set = {1, 4, 2, 67}
w_set = {22, 32, 11, 12, 2}

q_set |= w_set
print(q_set)
#------------------------------------------------

e_set = {51, 4, 2, 1}
r_set = {8, 35, 25, 5, 9}

e_set &= r_set
print(e_set)
#------------------------------------------------

t_set = {126, 'asdasd', 2, 4.68}
y_set = {2, 'asdasd', 5.5, 22}

t_set -= y_set
print(t_set)
#-----------------------------------------------

z_set = {'asdasdasds', 0, 24, 45, 79}
x_set = {89, 'asdasd', 'asdasdsdsa', 11, 54}

z_set ^= x_set
print(z_set)