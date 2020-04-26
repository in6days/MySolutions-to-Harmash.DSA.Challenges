#رسم أشكال هندسية - التحدي الرابع

# Enter the number of lines: 9
#   * * * * * * * *
# *   * * * * * * *
# * *   * * * * * *
# * * *   * * * * *
# * * * *   * * * *
# * * * * *   * * *
# * * * * * *   * *
# * * * * * * *   *
# * * * * * * * *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    if i == 1:
        print('  ' + '* ' * (l - 1), end='')
    if 1 < i < l:
        print('* ' * (i - 1) + '  ' + '* ' * (l - i), end='')
    if i == l:
        print('* ' * (l - 1) + '  ', end='')

    print()

#إنتبه: يجب أن يدخل المستخدم عدد مفرد و أكبر من صفر, مع الإشارة إلى أنه في حال قام بإدخال عدد مزدوج يجب أن يتم قبوله مع إضافة واحد عليه حتى يصبح مفرد.
Enter the number of lines: 9
  * * * * * * *
*   * * * * *   *
* *   * * *   * *
* * *   *   * * *
* * * *   * * * *
* * *   *   * * *
* *   * * *   * *
*   * * * * *   *
  * * * * * * *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i == j or i == l - j + 1:
            print('  ', end='')
        else:
            print('* ', end='')

    print()

# Enter the number of lines: 9
# *               *
#   *           *
#     *       *
#       *   *
#         *
#       *   *
#     *       *
#   *           *
# *               *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i == j or i == l - j + 1:
            print('* ', end='')
        else:
            print('  ', end='')

    print()

# Enter the number of lines: 9
# * * * * * * * * *
# * *           * *
# *   *       *   *
# *     *   *     *
# *       *       *
# *     *   *     *
# *   *       *   *
# * *           * *
# * * * * * * * * *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i == 1 or i == j or i == l - j + 1 or i == l or j == 1 or j == l:
            print('* ', end='')
        else:
            print('  ', end='')

    print()

# Enter the number of lines: 9
# * * * * * * * * *
# *       *       *
# *       *       *
# *       *       *
# * * * * * * * * *
# *       *       *
# *       *       *
# *       *       *
# * * * * * * * * *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i == 1 or i == l or i == int(l / 2) + 1 or j == 1 or j == l or j == int(l / 2) + 1:
            print('* ', end='')
        else:
            print('  ', end='')

    print()

#in6days