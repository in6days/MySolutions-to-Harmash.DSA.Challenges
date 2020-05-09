#إجراء عمليات حسابية - التحدي الأول

# أكتب برنامج يطلب من المستخدم إدخال رقم أكبر من 0, ثم يعرض له ناتج جمع جميع الأرقام من 1 لهذا الرقم.
# Enter a number: 5
# sum = 1 + 2 + 3 + 4 + 5
# Sum = 15
n = int(input('Enter a number: '))
sum = 0

print('sum = ', end='')

for i in range(1, n + 1):

    print(i, end=' ')

    if i < n:
        print('+', end=' ')

    sum += i

print('\nSum =', sum)

# أكتب برنامج يطلب من المستخدم إدخال رقم أكبر من 0, ثم يعرض له ناتج ضرب جميع الأرقام من 1 لهذا الرقم.
# Enter a number: 5
# M = 1 * 2 * 3 * 4 * 5
# M = 120
n = int(input('Enter a number: '))
m = 1

print('M = ', end='')

for i in range(1, n + 1):

    print(i, end=' ')

    if i < n:
        print('*', end=' ')

    m *= i

print('\nM =', m)

# أكتب برنامج يطلب من المستخدم إدخال رقمين, ثم يعرض له من هو العدد الأكبر بينهما, و في حال كانا متساويان سيعرض له أنهما كذلك.
# Enter first number: 3
# Enter second number: 8
# The biggest number is: 8
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if a==b:
    print('They are equal')
else:
    print('The biggest number is:', max(a,b))

# أكتب برنامج يطلب من المستخدم إدخال رقمين, ثم يعرض له من هو العدد الأصغر بينهما, و في حال كانا متساويان سيعرض له أنهما كذلك.
# Enter first number: 3
# Enter second number: 8
# The lowest number is: 3
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if a==b:
    print('They are equal')
else:
    print('The lowest number is:', min(a,b))

# أكتب برنامج يطلب من المستخدم إدخال رقمين, ثم يعرض له ناتج جمعمها, طرحهما, ضربهما و قسمتهما.
# Enter first number: 14
# Enter second number: 5
# 14+5= 19
# 14-5= 9
# 14*5= 70
# 14/5= 2
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

print('\n'+str(a)+'+'+str(b)+'=', a+b, end='')
print('\n'+str(a)+'-'+str(b)+'=', a-b, end='')
print('\n'+str(a)+'*'+str(b)+'=', a*b, end='')
print('\n'+str(a)+'/'+str(b)+'=', int(a/b), end='')

#in6days.