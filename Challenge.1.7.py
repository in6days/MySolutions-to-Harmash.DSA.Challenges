# رسم أشكال هندسية - التحدي السابع

# أكتب برنامج مهمته رسم الشكل التالي بواسطة الحلقات و حاول كتابة أصغر كود ممكن.
# عند تشغيل البرنامج, يجب أن يطلب من المستخدم إدخال عدد أسطر الشكل الذي سيتم رسمه.
# إنتبه: يجب أن يدخل المستخدم عدد مفرد و أكبر من صفر, لأن عدد الأسطر لا يمكن أن يكون مزدوجاً أو قيمته تساوي صفر أو أقل من صفر.
# Enter the number of lines: 11
# *                   *
# * *               * *
# *   *           *   *
# *     *       *     *
# *       *   *       *
# *         *         *
# *       *   *       *
# *     *       *     *
# *   *           *   *
# * *               * *
# *                   *
l = 0
while l <= 0 or l%2==0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i == j or i == l - j + 1 or j == 1 or j == l:
            print('* ', end='')
        else:
            print('  ', end='')

    print()

# Enter the number of lines: 11
# * * * * * * * * * * *
#   *               *
#     *           *
#       *       *
#         *   *
#           *
#         *   *
#       *       *
#     *           *
#   *               *
# * * * * * * * * * * *
l = 0
while l <= 0 or l%2==0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if i == j or i == l - j + 1 or i == 1 or i == l:
            print('* ', end='')
        else:
            print('  ', end='')

    print()

#Enter the number of lines: 11
# *                   *
# * *               * *
# *   *           *   *
# *     *       *     *
# * * * * *   * * * * *
#
# * * * * *   * * * * *
# *     *       *     *
# *   *           *   *
# * *               * *
# *                   *
l = 0
while l <= 0 or l % 2 == 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if (i == j or i == l - j + 1 or i == int(l / 2) or i == int(l / 2 + 2) or j == 1 or j == l) \
                and i != int(l / 2 + 1) and j != int(l / 2 + 1):
            print('* ', end='')
        else:
            print('  ', end='')

    print()

#Enter the number of lines: 11
# * * * * *   * * * * *
#   *     *   *     *
#     *   *   *   *
#       * *   * *
#         *   *
#
#         *   *
#       * *   * *
#     *   *   *   *
#   *     *   *     *
# * * * * *   * * * * *
l = 0
while l <= 0 or l % 2 == 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if (i == j or i == l - j + 1 or i == 1 or i == l or j == int(l / 2) or j == int(l / 2 + 2)) \
                and i != int(l / 2 + 1) and j != int(l / 2 + 1):
            print('* ', end='')
        else:
            print('  ', end='')

    print()

#Enter the number of lines: 11
# * * * * *   * * * * *
# *       *   *       *
# *       *   *       *
# *       *   *       *
# * * * * *   * * * * *
#
# * * * * *   * * * * *
# *       *   *       *
# *       *   *       *
# *       *   *       *
# * * * * *   * * * * *
l = 0
while l <= 0 and l % 2 == 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    for j in range(1, l + 1):
        if (i == 1 or i == l or i == int(l / 2) or i == int(l / 2) + 2 or j == 1 or j == l or j == int(
                l / 2) or j == int(l / 2) + 2) \
                and i != int(l / 2) + 1 and j != int(l / 2) + 1:
            print('* ', end='')
        else:
            print('  ', end='')

    print()

#in6days