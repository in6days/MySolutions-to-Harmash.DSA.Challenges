#إجراء عمليات حسابية - التحدي السادس

# أكتب برنامج يطلب من المستخدم إعطائه عدد صحيح أكبر من صفر و خزنه في المتغير n.
# بعدها يقوم بحساب القيمة النهائية التي سيتم تخزينها في المتغير s.
# Enter a number: 4
# S = 1 + 4 + 27 + 256
# S = 288
n = 0
s = 0

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    print(i ** i, end=' ')

    if i < n:
        print('+', end=' ')

    s += (i ** i)

print('\nS =', s)

# Enter a number: 4
# S = - 1 + 4 - 27 + 256
# S = 232
n = 0
s = 0

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    if i % 2 == 0:
        s += (i ** i)
        print('+', i ** i, end=' ')
    else:
        s -= (i ** i)
        print('-', i ** i, end=' ')

print('\nS =', s)

# Enter a number: 4
# S = + 1 + 4 + 3 + 256
# S = 264
n = 0
s = 0

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    if i % 2 == 0:
        s += (i ** i)
        print('+', i ** i, end=' ')
    else:
        s += i
        print('+', i, end=' ')

print('\nS =', s)

# Enter a number: 4
# S = + 1 - 4 + 3 - 256
# S = -256
n = 0
s = 0

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    if i % 2 == 0:
        s -= (i ** i)
        print('-', i ** i, end=' ')
    else:
        s += i
        print('+', i, end=' ')

print('\nS =', s)

# Enter a number: 4
# S = + 4 + 256
# S = 260
n = 0
s = 0

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    if i % 2 == 0:
        s += (i ** i)
        print('+', i ** i, end=' ')

print('\nS =', s)

#in6days.