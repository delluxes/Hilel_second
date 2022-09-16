import time


first = 'First deco'
second= 'Second deco'


def number_sub(start, end):
    if start < end:
        end, start = start, end
    return start - end
try:
    first = int(input('Enter the first number: '))
    second = int(input('Enter the second number: '))
    print(f'Your result is: {number_sub(first, second)}')
except ValueError:
    print('Your value is incorrect!')

##############################################################################

def timer (sec: int) -> str:
    if sec < 86400:
        days = 0
        resq = time.gmtime(sec)
        result = f'{str(days)}: {str(time.strftime("%H:%M:%S", resq))}'
        return result
    else:
        days = sec // 86400
        left_seconds = sec - (days * 86400)
        resq = time.gmtime(left_seconds)
        result = f'{str(days)}:{str(time.strftime("%H:%M:%S", resq))}'
        return result

print(f'{timer(86400) }')

################################################################################

sum_list = [2, 10, 24, 21, 50, 125]

def summery_for(x):
    null = 0
    for i in sum_list:
        null = null + i
    return null
print(f'Your summery: {summery_for(sum_list)}')

def summery_while(x):
    a = 0
    while a < len(x):
        b = sum(x)
        a += 1
    return b
print(f'Your summery: {summery_while(sum_list)}')

def summery_rekursion(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + summery_rekursion(x[1:])
print(f'Your summery: {summery_rekursion(sum_list)}')

################################################

a = int(input('Enter your number: '))
def fibanacci(i):
    if i <= 1:
        return 0
    elif i == 2:
        return 1
    return fibanacci(i - 1) + fibanacci(i - 2)

print(f'{fibanacci(a)= }')

##############################################
print(f'\n First: \n')
def sendvich(func):
    def tomato():
        print('tomato')

    def meat():
        print('meat')

    def cheese():
        print('cheese')

    def bread():
        print('bread')
    return tomato(), meat(), cheese(), bread()


@sendvich
def sendv() -> any:
    return

print(f'\n Second: \n')


def tomato(decor_this):
    print('tomato')


def meat(decor_this):
    print('meat')


def cheese(decor_this):
    print('cheese')


def bread(decor_this):
    print('bread')

@tomato
@meat
@cheese
@bread
def sendv() -> any:
    return


