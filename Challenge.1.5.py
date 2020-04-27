#رسم أشكال هندسية - التحدي الخامس

# إنتبه: يجب أن يدخل المستخدم عدد مفرد و أكبر من صفر, لأن عدد الأسطر لا يمكن أن يكون مزدوجاً أو قيمته تساوي صفر أو أقل من صفر.
# Enter the number of lines: 9
#         * * * * *
#         * * * * *
#         * * * * *
#         * * * * *
# * * * * * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
l = 0
while l <= 0 and l % 2 == 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    if i <= (l / 2):
        print('  ' * int(l / 2) + '* ' + '* ' * int(l / 2), end='')
    if i == int(l / 2 + 1):
        print('* ' * l, end='')
    if (l / 2 + 1) < i <= l:
        print('* ' * int(l / 2) + '* ' + '  ' * int(l / 2), end='')

    print()

# Enter the number of lines: 9
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * * * * * *
#         * * * * *
#         * * * * *
#         * * * * *
#         * * * * *
l = 0
while l <= 0 and l % 2 == 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l+1):
    if i <= (l/2):
        print('* ' * int(l / 2) + '* ' + '  ' * int(l/2), end='')
    if i == int(l/2 +1):
        print('* ' * l, end='')
    if (l/2 +1) < i <= l:
        print( '  '* int(l/2) + '* ' + '* ' * int(l/2), end='')

    print()

# Enter the number of lines: 9
#         * * * * *
#         *       *
#         *       *
#         *       *
# * * * * * * * * *
# *       *
# *       *
# *       *
# * * * * *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i == int(l / 2) + 1 or j == int(l / 2) + 1 or (i == 1 and j > int(l / 2) + 1) or (
                i == l and j < int(l / 2) + 1) or (j == l and i < int(l / 2) + 1) or (j == 1 and i > int(l / 2) + 1):
            print('* ', end='')
        else:
            print('  ', end='')

    print()

# Enter the number of lines: 9
# * * * * *
# *       *
# *       *
# *       *
# * * * * * * * * *
#         *       *
#         *       *
#         *       *
#         * * * * *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i == int(l / 2) + 1 or j == int(l / 2) + 1 or (i == 1 and j < int(l / 2) + 1) or (
                i == l and j > int(l / 2) + 1) or (j == l and i > int(l / 2) + 1) or (j == 1 and i < int(l / 2) + 1):
            print('* ', end='')
        else:
            print('  ', end='')

    print()

# Enter the number of lines: 7
# * 1 1 1 1 1 1
# 0 * 1 1 1 1 1
# 0 0 * 1 1 1 1
# 0 0 0 * 1 1 1
# 0 0 0 0 * 1 1
# 0 0 0 0 0 * 1
# 0 0 0 0 0 0 *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i == j:
            print('* ', end='')
        if i > j:
            print('0 ', end='')
        if i < j:
            print('1 ', end='')

    print()

#in6days