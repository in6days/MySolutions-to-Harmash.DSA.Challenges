#رسم أشكال هندسية - التحدي الثامن

#Enter the number of lines: 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        print(j, end=' ')
    print()

#Enter the number of lines: 7
# 1 1 1 1 1 1 1
# 2 2 2 2 2 2 2
# 3 3 3 3 3 3 3
# 4 4 4 4 4 4 4
# 5 5 5 5 5 5 5
# 6 6 6 6 6 6 6
# 7 7 7 7 7 7 7
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        print(i, end=' ')
    print()

#Enter the number of lines: 7
Enter the number of lines: 7
# 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i % 2 == 1:
            print(1, end=' ')
        if i % 2 == 0:
            print(0, end=' ')
    print()

#Enter the number of lines: 7
# 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if j % 2 == 1:
            print(1, end=' ')
        if j % 2 == 0:
            print(0, end=' ')

    print()

#Enter the number of lines: 7
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0
# 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):

        if (i % 2 == 1 and j % 2 == 1) or (i % 2 == 0 and j % 2 == 0):
            print(0, end=' ')
        else:
            print(1, end=' ')

    print()

#in6days.