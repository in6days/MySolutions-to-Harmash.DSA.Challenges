#إجراء عمليات حسابية - التحدي الثاني

# أكتب برنامج يطلب من المستخدم إدخال رقمين, ثم يعرض له نتيجة مقارنة هذين الرقمين.
# Enter first number: 7
# Enter second number: 2
# Result: 7 > 2
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if a<b:
    print('\nResult:',a,'<',b)
elif a>b:
    print('\nResult:',a,'>',b)
else:
    print('\nResult:',a,'=',b)

# أكتب برنامج يطلب من المستخدم إدخال ثلاث أرقام و خزنها في ثلاث متغيرات (a - b - c ), ثم يعرض له أكبر رقم تم إداخله.
# Enter a: 2
# Enter b: 7
# Enter c: 5
# The max number is: 7
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

print('The max number is:', max(a, b, c))

# أكتب برنامج يطلب من المستخدم إدخال ثلاث أرقام و خزنها في ثلاث متغيرات (a - b - c ), ثم يعرض له أصغر رقم تم إداخله.
# Enter a: 2
# Enter b: 7
# Enter c: 5
# The max number is: 2
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

print('The max number is:', min(a, b, c))

#أكتب برنامج عند تشغيله يقوم بطباعة جدول الضرب من 1 إلى 10 مع وضع سطر فارغ بين كل جدولين كالتالي.
for i in range(1, 11):
    print('\n')

    for j in range(1, 11):
        print(i, '*', j, '=', i * j)

# أكتب برنامج يطلب من المستخدم إدخال رقمين, ثم يعرض له قائمة خيارات يمكن تطبيقها على هذين الرقمين.
# المستخدم سيكون عليه إدخال رقم الخيار فقط حتى يتم تنفيذه.
# الخيار 0 لإيقاف البرنامج.
# الخيار 1 لإطباعة ناتج جمع العددين.
# الخيار 2 لإطباعة ناتج طرح العددين.
# الخيار 3 لإطباعة ناتج شرب العددين.
# الخيار 4 لإطباعة ناتج قسمة العددين
# Enter first number: 1
# Enter second number: 4
# Write down the operation number then press enter
# 0: To end the program.
# 1: To print the sum.
# 2: To print the subtraction.
# 3: To print the multiplication.
# 4: To print the division.
# ------------------------
# Enter option: 2
# 1 - 4 = -3
# --------------
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

print("\nWrite down the operation number then press enter\n"
      "0: To end the program.\n"
      "1: To print the sum.\n"
      "2: To print the subtraction.\n"
      "3: To print the multiplication.\n"
      "4: To print the division.\n"
     "------------------------")

o = int(input('Enter option: '))

if o==0:
    print('program end.')
elif o==1:
    print(a, '+', b, '=', a+b,'\n--------------')
elif o==2:
    print(a, '-', b, '=', a-b,'\n--------------')
elif o==3:
    print(a, '*', b, '=', a*b,'\n--------------')
elif o==4:
    print(a, '/', b, '=', a/b, '\n--------------')

#in6days.
