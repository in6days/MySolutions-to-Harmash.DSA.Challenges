#رسم أشكال هندسية - التحدي التاسع

#ملاحظة: هنا افترضنا أن المستخدم قام بإدخال الرقم 3 عند التشغيل
# Enter the number of lines: 3
# 1 1 1 1 1 1
# 2 2 2 2 2 2
# 3 3 3 3 3 3
# 3 3 3 3 3 3
# 2 2 2 2 2 2
# 1 1 1 1 1 1
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, (2 * l) + 1):
    for j in range(1, (2 * l) + 1):

        if i <= l:
            print(i, end=' ')
        else:
            print((2 * l - (i - 1)), end=' ')

    print()

#Enter the number of lines: 3
# 1 2 3 3 2 1
# 1 2 3 3 2 1
# 1 2 3 3 2 1
# 1 2 3 3 2 1
# 1 2 3 3 2 1
# 1 2 3 3 2 1
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, (2 * l) + 1):
    for j in range(1, (2 * l) + 1):

        if j <= l:
            print(j, end=' ')
        else:
            print((2 * l - (j - 1)), end=' ')

    print()

# Enter the number of lines: 6
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i >= j:
            print(i, end=' ')

    print()

#Enter the number of lines: 6
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i >= j:
            print(j, end=' ')

    print()

# Enter the number of lines: 6
# 1 1 1 1 1 1
# 1 2 2 2 2 2
# 1 2 3 3 3 3
# 1 2 3 4 4 4
# 1 2 3 4 5 5
# 1 2 3 4 5 6
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):

        if i >= j:
            print(j, end=' ')
        else:
            print(i, end=' ')

    print()

#in6days.