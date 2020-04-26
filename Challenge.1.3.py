#رسم أشكال هندسية - التحدي الثالث

# أكتب برنامج مهمته رسم الشكل التالي بواسطة الحلقات.
# عند تشغيل البرنامج, يجب أن يطلب من المستخدم إدخال عدد أسطر الشكل الذي سيتم رسمه.
# إنتبه: يجب أن يدخل المستخدم عدد مفرد و أكبر من صفر, لأن عدد الأسطر لا يمكن أن يكون مزدوجاً أو قيمته تساوي صفر أو أقل من صفر.
# Enter the number of lines: 9
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
l = 0  # lines
while l <= 0 or l % 2 == 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l + 1):
    if i <= (l / 2):
        print(' ' * (int(l / 2) + 1 - i) + '*' * i + '*' * (i - 1) + ' ' * (int(l / 2) + 1 - i), end='')

    else:
        print(' ' * (i - (int(l / 2) + 1)) + '*' * (l - i) + '*' + '*' * (l - i) + ' ' * (i - (int(l / 2) + 1)), end='')

    print()

#إنتبه: يجب أن يدخل المستخدم عدد مفرد و أكبر من صفر, لأن عدد الأسطر لا يمكن أن يكون مزدوجاً أو قيمته تساوي صفر أو أقل من صفر.
# Enter the number of lines: 9
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
l = 0
while l <= 0 or l % 2 == 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l+1):
    if i==1:
        print(' '*(int(l/2)+1-i)+'*'+' '*(int(l/2)+1-i), end='')
    if 1<i<=(l/2):
        print(' '*abs(int(l/2)+1-i)+'*'+' '*(i-1)+' '*(i-2)+'*'+' '*abs((int(l/2)+1)-i), end='')
    if (l/2)<i<l:
        print(' '*((i-int(l/2))-1)+'*'+' '*((2*int(l/2))-i)+' '+' '*((2*int(l/2))-i)+'*'+' '*((i-int(l/2))-1), end='')
    if i==l:
        print(' '*(i-1-int(l/2))+'*'+' '*(i-1-int(l/2)))

    print()

# #إنتبه: يجب أن يدخل المستخدم عدد مفرد و أكبر من صفر, لأن عدد الأسطر لا يمكن أن يكون مزدوجاً أو قيمته تساوي صفر أو أقل من صفر.
# Enter the number of lines: 9
# ----*----
# ---* *---
# --*   *--
# -*     *-
# *       *
# -*     *-
# --*   *--
# ---* *---
# ----*----
l = 0
while l <= 0 or l % 2 == 0:
    l = int(input('Enter the number of lines: '))

for i in range(1, l+1):
    if i==1:
        print('-'*(int(l/2)+1-i)+'*'+'-'*(int(l/2)+1-i), end='')
    if 1<i<=(l/2):
        print('-'*abs(int(l/2)+1-i)+'*'+' '*(i-1)+' '*(i-2)+'*'+'-'*abs((int(l/2)+1)-i), end='')
    if (l/2)<i<l:
        print('-'*((i-int(l/2))-1)+'*'+' '*((2*int(l/2))-i)+' '+' '*((2*int(l/2))-i)+'*'+'-'*((i-int(l/2))-1), end='')
    if i==l:
        print('-'*(i-1-int(l/2))+'*'+'-'*(i-1-int(l/2)))

    print()

# إنتبه: يجب أن يدخل المستخدم عدد أكبر من صفر, لأن عدد الأسطر أو الأعمدة لا يمكن أن يكون صفر أو أقل من صفر.
# Enter the number of length: 10
# * * * * * * * * * *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# * * * * * * * * * *
L = 0
while L <= 0:
    L = int(input('Enter the number of length: '))

for i in range(1, L + 1):
    if i == 1 or i == (L - 1):
        print('* ' * (L))
    if 1 <= i < (L - 1):
        print('*' + '  ' * (L - 2) + ' *', end='')

    print()

# إنتبه: يجب أن يدخل المستخدم عددين أكبر من صفر, لأن عدد أسطر و أعمدة الرسمة لا يمكن أن يكون صفر أو أقل من صفر.
# Enter the number of lines: 7
# Enter the number of columns: 15
# * * * * * * * * * * * * * * *
# *                           *
# *                           *
# *                           *
# *                           *
# *                           *
# * * * * * * * * * * * * * * *
l = 0
c = 0
while l <= 0:
    l = int(input('Enter the number of lines: '))

while c <= 0:
    c = int(input('Enter the number of columns: '))

for i in range(1, l + 1):
    if i == 1 or i == (l - 1):
        print('* ' * c)
    if 1 <= i < (l - 1):
        print('*' + '  ' * (c - 2) + ' *', end='')

    print()

#in6days