#رسم أشكال هندسية - التحدي السادس

#إنتبه: يجب أن يدخل المستخدم عدد مفرد و أكبر من صفر, لأن عدد الأسطر لا يمكن أن يكون مزدوجاً أو قيمته تساوي صفر أو أقل من صفر.
# Enter the number of lines: 9
# *               *
# * *           * *
# * * *       * * *
# * * * *   * * * *
# * * * * * * * * *
# * * * *   * * * *
# * * *       * * *
# * *           * *
# *               *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    if i <= int(l / 2):
        print('* ' * i + '  ' * (l - (2 * i)) + '* ' * i, end='')
    if i == int(l / 2 + 1):
        print('* ' * l, end='')
    if i > int(l / 2 + 1):
        print('* ' * (l - i + 1) + '  ' * (2 * (i - 1) - l) + '* ' * (l - i + 1), end='')

    print()

# Enter the number of lines: 9
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    if i <= int(l / 2 + 1):
        print('  ' * (i - 1) + '* ' * (l - 2 * (i - 1)), end='')
    if i > int(l / 2 + 1):
        print('  ' * (l - i) + '* ' * ((2 * i) - l), end='')

    print()

#Enter the number of lines: 9
# *               *
# * *           * *
# * * *       * * *
# * * * *   * * * *
#
# * * * *   * * * *
# * * *       * * *
# * *           * *
# *               *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    if i <= int(l / 2):
        print('* ' * i + '  ' * (l - (2 * i)) + '* ' * i, end='')
    if i == int(l / 2 + 1):
        print('  ' * l, end='')
    if i > int(l / 2 + 1):
        print('* ' * (l - i + 1) + '  ' * (2 * (i - 1) - l) + '* ' * (l - i + 1), end='')

    print()

# Enter the number of lines: 9
# * * * *   * * * *
#   * * *   * * *
#     * *   * *
#       *   *
#
#       *   *
#     * *   * *
#   * * *   * * *
# * * * *   * * * *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    if i < int(l / 2 + 1):
        print('  ' * (i - 1) + '* ' * int((l - 2 * (i - 1)) / 2) + '  ' + '* ' * int((l - 2 * (i - 1)) / 2), end='')
    if i > int(l / 2 + 1):
        print('  ' * (l - i) + '* ' * int(((2 * i) - l) / 2) + '  ' + '* ' * int(((2 * i) - l) / 2), end='')

    print()
#Enter the number of lines: 9
# * * * *   * * * *
# * * * *   * * * *
# * * * *   * * * *
# * * * *   * * * *
#
# * * * *   * * * *
# * * * *   * * * *
# * * * *   * * * *
# * * * *   * * * *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))
if l % 2 == 0:
    l = l + 1

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i == int(l / 2 + 1) or j == int(l / 2 + 1):
            print('  ', end='')
        else:
            print('* ', end='')
    print()

#in6days.