#رسم أشكال هندسية - التحدي الثاني

#أكتب برنامج مهمته رسم الشكل التالي بواسطة الحلقات.
#.عند تشغيل البرنامج, يجب أن يطلب من المستخدم إدخال عدد أسطر و أعمدة الشكل الذي سيتم رسمه
#إنتبه: يجب أن يدخل المستخدم عددين أكبر من صفر, لأن عدد أسطر و أعمدة الرسمة لا يمكن أن يكون صفر أو أقل من صفر.
# Enter the number of lines: 5
# Enter the number of columns: 10
# ******
#  ******
#   ******
#    ******
#     ******
l = 0
c = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

while c <= 0:
    c = int(input('Enter the number of columns: '))

for i in range(1, l + 1):
    print(' ' * (i - 1) + '*' * ((c - l) + 1) + ' ' * (l - 1))

#إنتبه: يجب أن يدخل المستخدم عدد أكبر من صفر, لأن عدد الأسطر لا يمكن أن يكون صفر أو أقل من صفر.
# Enter the number of lines: 7
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    print(' ' * (l - i) + ('*' * i) + '*' * (i - 1) + ' ' * (l - i))

# إنتبه: يجب أن يدخل المستخدم عدد أكبر من صفر, لأن عدد الأسطر لا يمكن أن يكون صفر أو أقل من صفر.
# Enter the number of lines: 7
# *************
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
l = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    print(' ' * (i - 1) + '*' * (l - i) + '*' + '*' * (l - i) + ' ' * (i - 1))

# إنتبه: يجب أن يدخل المستخدم عدد مفرد و أكبر من صفر, لأن عدد الأسطر لا يمكن أن يكون مزدوجاً أو قيمته تساوي صفر أو أقل من صفر
# Enter the number of lines: 9
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
l = 0
while l <= 0 or l % 2 == 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):

    if i <= (l / 2):
        print('*' * i, end='')
    else:
        print('*' * (l - i + 1), end='')

    print()

# إنتبه: يجب أن يدخل المستخدم عدد مفرد و أكبر من صفر, لأن عدد الأسطر لا يمكن أن يكون مزدوجاً أو قيمته تساوي صفر أو أقل من صفر
# Enter the number of lines: 9
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *
l = 0
while l <= 0 or l % 2 == 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    if i <= (l / 2):
        print(' ' * (int(l / 2) + 1 - i) + '*' * i, end='')

    else:
        print(' ' * (i - (int(l / 2) + 1)) + '*' * (l - i + 1), end='')

    print()

#in6days
