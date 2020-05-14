#إجراء عمليات حسابية - التحدي السابع

# أكتب برنامج يطلب من المستخدم إعطائه عدد صحيح أكبر من صفر و خزنه في المتغير n.
# بعدها يقوم بحساب القيمة النهائية التي سيتم تخزينها في المتغيرين s و t.
# Enter a number: 4
# S = 7
# T = 26

n = 0
s = 0
t = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

for i in range(1, n + 1):

    fact *= i

    if i % 2 == 1:
        s += fact
    else:
        t += fact

print('S =', s)
print('T =', t)

# Enter a number: 4
# S = 0.5 + 0.25 + 0.1111111111111111 + 0.03571428571428571
# S = 0.8968253968253969
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    fact *= i

    print(1 / (i + fact), end=' ')

    if i < n:
        print('+', end=' ')

    s += 1 / (i + fact)

print('\nS =', s)

# Enter a number: 4
# S = + 1 + 0.5 + 3 + 0.041666666666666664
# S = 4.541666666666667
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
        print('+', 1 / fact, end=' ')
    else:
        s += i
        print('+', i, end=' ')

print('\nS =', s)

# Enter a number: 4
# S = 0.3333333333333333 + 0.4 + 0.3 + 0.13793103448275862
# S = 1.1712643678160921
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    fact *= i

    print(i / ((i + 1) + fact), end=' ')

    if i < n:
        print('+', end=' ')

    s += i / ((i + 1) + fact)

print('\nS =', s)

# Enter a number: 4
# S = - 3 + 8 - 27 + 124
# S = 102
n = 0
s = 0
fact = 1

while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    fact *= (i + 1)

    if i % 2 == 1:
        s -= (i + fact)
        print('-', str(i + fact), end=' ')
    else:
        s += (i + fact)
        print('+', str(i + fact), end=' ')

print('\nS =', s)

#in6days.