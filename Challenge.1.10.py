#رسم أشكال هندسية - التحدي العاشر

#عند تشغيل البرنامج, يجب أن يطلب من المستخدم إدخال عدد بين 1 و 9 حتى يتم رسم الشكل المطلوب بناءاً عليه.
# Enter the number of lines: 6
# 1
# 1 2
# 1   3
# 1     4
# 1       5
# 1 2 3 4 5 6
l = 0
while l <= 0 or l > 9:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):

        if j == 1 or j == i or i == l:
            print(j, end=' ')
        else:
            print(' ', end=' ')

    print()

# Enter the number of lines: 6
# 6
# 6 5
# 6   4
# 6     3
# 6       2
# 6 5 4 3 2 1
l = 0
while l <= 0 or l > 9:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):

        if j == 1 or j == i or i == l:
            print((l - j + 1), end=' ')
        else:
            print(' ', end=' ')

    print()

# Enter the number of lines: 6
#           1
#         1 2
#       1   3
#     1     4
#   1       5
# 1 2 3 4 5 6
l = 0
while l <= 0 or l > 9:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):

        if j == (l - i + 1):
            print(1, end=' ')
        elif j == l:
            print(i, end=' ')
        elif i == l:
            print(j, end=' ')
        else:
            print(' ', end=' ')

    print()

# Enter the number of lines: 6
#           6
#         6 5
#       6   4
#     6     3
#   6       2
# 6 5 4 3 2 1
l = 0
while l <= 0 or l > 9:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):

        if j == (l - i + 1):
            print(l, end=' ')
        elif j == l:
            print((l - i + 1), end=' ')
        elif i == l:
            print((l - j + 1), end=' ')
        else:
            print(' ', end=' ')

    print()

# Enter the number of lines: 6
# 6 5 4 3 2 1
# 6       2
# 6     3
# 6   4
# 6 5
# 6
l = 0
while l <= 0 or l > 9:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):

        if i == 1 or j == 1 or j == (l - i + 1):
            print((l - j + 1), end=' ')
        else:
            print(' ', end=' ')

    print()

#in6days.