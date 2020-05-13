#إجراء عمليات حسابية - التحدي الخامس

# أكتب برنامج يطلب من المستخدم إعطائه عدد صحيح أكبر من صفر و خزنه في المتغير n.
# بعدها يقوم بحساب القيمة النهائية التي سيتم تخزينها في المتغير s.
# Enter a number: 4
# S = 1! + 2! + 3! + 4!
# S = 33
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    print(str(i) + '!', end=' ')

    if i < n:
        print('+', end=' ')

    fact *= i
    s += fact

print('\nS =', s)

# Enter a number: 4
# S = + 1! - 2! + 3! - 4!
# S = -19
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    fact *= i

    if i % 2 == 0:
        s -= fact
        print('-', str(i) + '!', end=' ')
    else:
        s += fact
        print('+', str(i) + '!', end=' ')

print('\nS =', s)

# Enter a number: 4
# S = + 1 + 2! + 3 + 4!
# S = 30
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    fact *= i

    if i % 2 == 0:
        s += fact
        print('+', str(i) + '!', end=' ')
    else:
        s += i
        print('+', i, end=' ')

print('\nS =', s)

# Enter a number: 4
# S = - 1 + 2! - 3 + 4!
# S = 22
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    fact *= i

    if i % 2 == 0:
        s += fact
        print('+', str(i) + '!', end=' ')
    else:
        s -= i
        print('-', i, end=' ')

print('\nS =', s)

# Enter a number: 4
# S = + 2! + 4!
# S = 26
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    fact *= i

    if i % 2 == 0:
        s += fact
        print('+', str(i) + '!', end=' ')

print('\nS =', s)

#in6days.
