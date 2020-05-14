#إجراء عمليات حسابية - التحدي الثامن

# أكتب برنامج يطلب من المستخدم إعطائه عدد صحيح أكبر من صفر و خزنه في المتغير n.
# بعدها يقوم بحساب القيمة النهائية التي سيتم تخزينها في المتغير s.
# Enter a number: 4
# S = + 1 + 2 + 27 + 24
# S = 54
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
        print('+', str(fact), end=' ')
    else:
        s += i ** i
        print('+', str(i ** i), end=' ')

print('\nS =', s)

# Enter a number: 4
# S = + 1 + 0.5 + 27 + 0.041666666666666664
# S = 28.541666666666668
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    fact *= i
    if i % 2 == 0:
        s += 1 / fact
        print('+', str(1 / fact), end=' ')
    else:
        s += i ** i
        print('+', str(i ** i), end=' ')

print('\nS =', s)

# Enter a number: 4
# S = 1.0 + 2.0 + 4.5 + 10.666666666666666
# S = 18.166666666666664
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    fact *= i
    print((i**i)/fact, end=' ')

    if i < n:
        print('+', end=' ')

    s += (i**i)/fact

print('\nS =', s)

# Enter a number: 4
# S = 1.0 + 0.5 + 0.2222222222222222 + 0.09375
# S = 1.8159722222222223
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    fact *= i
    print(fact/(i**i), end=' ')

    if i < n:
        print('+', end=' ')

    s += fact/(i**i)

print('\nS =', s)

# Enter a number: 4
# S = + 1.0 - 2.0 + 0.2222222222222222 - 10.666666666666666
# S = -11.444444444444445
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    fact *= i

    if i % 2 == 0:
        s -= (i ** i) / fact
        print('-', str((i ** i) / fact), end=' ')
    else:
        s += fact / (i ** i)
        print('+', str(fact / (i ** i)), end=' ')

print('\nS =', s)

#in6days.