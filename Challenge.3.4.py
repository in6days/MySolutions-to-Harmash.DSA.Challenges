#إجراء عمليات حسابية - التحدي الرابع

# أكتب برنامج يطلب من المستخدم إعطائه عدد صحيح أكبر من صفر و خزنه في المتغير n.
# بعدها يقوم بحساب القيمة النهائية التي سيتم تخزينها في المتغير s.
# Enter a number: 4
# S = 1.0 + 0.5 + 0.3333333333333333 + 0.25
# S = 2.083333333333333
n = 0
s = 0
while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    print(1 / i, end=' ')

    if i < n:
        print('+', end=' ')

    s += 1 / i

print('\nS =', s)

# Enter a number: 4
# S = + 1.0 -0.5 + 0.3333333333333333 -0.25
# S = 0.5833333333333333
n = 0
s = 0
while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    if i % 2 == 0:
        s -= 1 / i
        print((-1) * (1 / i), end=' ')
    elif i % 2 == 1:
        s += 1 / i
        print('+', 1 / i, end=' ')

print('\nS =', s)

# Enter a number: 4
# S = 0.5 + 1.3333333333333333 + 2.25 + 3.2
# S = 7.283333333333333
n = 0
s = 0
while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    print((i * i) / (i + 1), end=' ')

    if i < n:
        print('+', end=' ')

    s += (i * i) / (i + 1)

print('\nS =', s)

# Enter a number: 4
# S = + 1.0 - 1.3333333333333333 + 1.5 - 1.6
# S = -0.43333333333333335
n = 0
s = 0
while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    if (i + 1) % 2 == 0:
        s += (2 * i) / (i + 1)
        print('+', (2 * i) / (i + 1), end=' ')
    elif (i + 1) % 2 == 1:
        s -= (2 * i) / (i + 1)
        print('-', (2 * i) / (i + 1), end=' ')

print('\nS =', s)

# Enter a number: 4
# S = + 1.0 - 2.0 + 3.0 - 4.0
# S = -2.0
n = 0
s = 0
while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    if (i + 1) % 2 == 0:
        s += (i * (i + 1)) / (i + 1)
        print('+', (i * (i + 1)) / (i + 1), end=' ')
    elif (i + 1) % 2 == 1:
        s -= (i * (i + 1)) / (i + 1)
        print('-', (i * (i + 1)) / (i + 1), end=' ')

print('\nS =', s)

#in6days.