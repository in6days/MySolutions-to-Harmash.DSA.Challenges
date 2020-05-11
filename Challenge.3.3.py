#إجراء عمليات حسابية - التحدي الثالث

# أكتب برنامج يطلب من المستخدم إدخال خمسة أعداد ثم يعرض له متوسط هذه الأعداد.
# ملاحظة: كل عدد يتم إدخاله يجب أن يتم تخزينه في متغير. أي ممنوع إستخدام مصفوفة
# Enter n1: 7
# Enter n2: 4
# Enter n3: 9
# Enter n4: 1
# Enter n5: 3
# Average =  4.8
n1 = float(input('Enter n1: '))
n2 = float(input('Enter n2: '))
n3 = float(input('Enter n3: '))
n4 = float(input('Enter n4: '))
n5 = float(input('Enter n5: '))

print('Average = ', (n1+n2+n3+n4+n5)/5)

# أكتب برنامج يطلب من المستخدم إدخال رقم الشهر, و بعدها سيقوم بطباعة إسم الشهر باللغة الإنجليزية.
# رقم الشهر يجب أن يكون بين 1 و 12
# Month number: 5
# Month name: May
n = int(input('Month number: '))

print('Month name: ', end='')

if n<1 or n>12:
    print('Error input, Month number should be between 1 and 12.')
elif n==1:
    print('January')
elif n==2:
    print('February')
elif n==3:
    print('March')
elif n==4:
    print('April')
elif n==5:
    print('May')
elif n==6:
    print('June')
elif n==7:
    print('July')
elif n==8:
    print('August')
elif n==9:
    print('September')
elif n==10:
    print('October')
elif n==11:
    print('November')
elif n==12:
    print('December	')

# أكتب برنامج يطلب من المستخدم إعطائه عدد صحيح أكبر من صفر و خزنه في المتغير n.
# بعدها يقوم بحساب ناتج جمع جميع الأرقام من 1 إلى n و يخزنها في متغير إسمه s
# Enter a number: 7
# S = 1 + 2 + 3 + 4 + 5 + 6 + 7
# S = 28
n = 0
s = 0
while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):

    print(i, end=' ')

    if i < n:
        print('+', end=' ')

    s += i

print('\nS =', s)

# أكتب برنامج يطلب من المستخدم إعطائه عدد صحيح أكبر من صفر و خزنه في المتغير n.
# بعدها يقوم بحساب ناتج ضرب جميع الأرقام من 1 إلى n و يخزنها في متغير إسمه m
# Enter a number: 7
# M = 1 * 2 * 3 * 4 * 5 * 6 * 7
# M = 5040
n = 0
m = 1
while n <= 0:
    n = int(input('Enter a number: '))

print('M = ', end='')

for i in range(1, n + 1):

    print(i, end=' ')

    if i < n:
        print('*', end=' ')

    m *= i

print('\nM =', m)

# أكتب برنامج يطلب من المستخدم إعطائه عدد صحيح أكبر من صفر و خزنه في المتغير n.
# بعدها يقوم بحساب القيمة النهائية التي سيتم تخزينها في المتغير s.
# Enter a number: 6
# S = -1 + 2 -3 + 4 -5 + 6
# S = 3
n = 0
s = 0
while n <= 0:
    n = int(input('Enter a number: '))

print('S = ', end='')

for i in range(1, n + 1):
    if i % 2 == 1:
        s += i * (-1)
        print(i * (-1), end=' ')
    elif i % 2 == 0:
        s += i
        print('+', i, end=' ')

print('\nS =', s)

#in6days.