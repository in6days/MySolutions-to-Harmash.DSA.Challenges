#إجراء عمليات حسابية - التحدي التاسع

# قم بتعريف دالة إسمها Power(), عند استدعاءها نمرر لها عددين, فترجع ناتج قيمة العدد الأول مضاعفة بقيمة العدد الثاني.
# Enter x: 2
# Enter y: 3
# 2 ^ 3 = 8
def power(x, y):
    return x ** y

x = int(input('Enter x: '))
y = int(input('Enter y: '))

result = power(x, y)

print(x, '^', y, '=', result, end='')

# قم بتعريف دالة إسمها Factorial(), عند استدعاءها نمرر لها عدد, فترجع ناتج قيمة الـ Factorial له.
# Enter n: 4
# 4! = 24
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input('Enter n: '))

print(str(n) + '! =', factorial(n), end='')

# قم بتعريف دالة إسمها SquareRoot(), عند استدعاءها نمرر لها عدد, فترجع ناتج قيمة الجزر التربيعي ( Square Root ) له.
# Enter x: 5
# √5 = 2.23606797749979
def squareRoot(x):
    if x >= 0:
        return x ** (1 / 2)
    else:
        return 'Enter the absolute value | | of the number'


x = int(input('Enter x: '))

print('√' + str(x), '=', squareRoot(x), end='')

# قم بتعريف دالة إسمها IsPrime(), عند استدعاءها نمرر لها عدد, فترجع True إذا كان العدد عبارة عن عدد أوّلي ( Prime Number ) و ترجع False إن لم يكن كذلك.
# Enter a number: 17
# Is 17 a prime number: True
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input('Enter a number: '))

print('Is', str(n), 'a prime number:', isPrime(n), end='')

# أكتب برنامج يطلب من المستخدم إعطائه عدد صحيح أكبر من 2 و خزنه في المتغير n.
# # بعدها يقوم بطباعة جميع الأعداد الأولية ( Prime Numbers ) الموجودة بين 2 و n.
 # Enter a number: 12
# All prime number between 2 and 12: 2 3 5 7 11
n = 1
while n <= 1:
    n = int(input('Enter a number: '))

print('All prime number between 2 and ' + str(n) + ': ', end='')

for i in range(2, n + 1):
    for j in range(2, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=' ')

#in6days.