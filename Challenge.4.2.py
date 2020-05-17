#التعامل مع المصفوفات - التحدي الثاني

# أكتب برنامج يطلب من المستخدم إعطائه عدد يمثل عدد عناصر مصفوفة إسمها array و يخزنه في متغير إسمه n.
# ملاحظة: عدد عناصر المصفوفة يجب أن يكون أكبر من صفر.
# بعدها ينشئ المصفوفة array و يحدد أن عدد عناصرها هو العدد الذي أدخله المستخدم.
# بعدها يطلب من المستخدم إدخال عدد صحيح لكل عنصر فيها.
# بعدها يعرض للمستخدم جميع قيم عناصر المصفوفة التي قام هو بإدخالها مع وضع مسافة فارغة بين كل قيمتين.
# بعدها يقوم بتحويل كل قيمة في المصفوفة أكبر من صفر إلى 1 و كل قيمة أصغر من صفر إلى -1.
# في الأخير, يقوم بعرض قيم المصفوفة من جديد.
# Enter number of array elements: 4
# Enter the elements:
# -2
# 0
# -5
# 7
# Array values: [-2, 0, -5, 7]
# Array -1 & 1 values: [-1, 0, -1, 1]
arr = []
n = 0

while n <= 0:
    n = int(input('Enter number of array elements: '))
print('Enter the elements:')
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print('Array values:', arr, end='')

for i in range(len(arr)):
    if arr[i] == 0:
        arr[i] = 0
    elif arr[i] < 0:
        arr[i] = -1
    else:
        arr[i] = 1

print('\nArray -1 & 1 values:', arr, end='')

# أكتب برنامج يقوم بتعريف ثلاث مصفوفات A و B و C.
# ثم يطلب من المستخدم إدخال عدد يمثل عدد عناصر المصفوفات الثلاثة.
# ملاحظة: عدد عناصر المصفوفات يجب أن يكون أكبر من صفر.
# بعدها يطلب من المستخدم إدخال قيم لجميع عناصر المصفوفتين A و B و يجمعهم في المصفوفة C.
# في الأخير, يعرض للمستخدم القيم التي أصبحت تحتويها المصفوفة C على سطر واحد مع وضع مسافة فارغة بين كل قيمتين
# Enter the number of array elements: 3
# Enter A elements:
# 1
# 2
# 3
# Enter B elements:
# 4
# 5
# 6
# C elements: Sum of A & B values
#
# A values: [1, 2, 3]
# B values: [4, 5, 6]
# C values: [5, 7, 9]
a = []
b = []
c = []
n = 0

while n <= 0:
    n = int(input('Enter the number of array elements: '))

print('Enter A elements:')
for i in range(0, n):
    ele = int(input())
    a.append(ele)

print('Enter B elements:')
for i in range(0, n):
    ele = int(input())
    b.append(ele)

print('C elements: Sum of A & B values')
for i in range(0, n):
    ele = a[i] + b[i]
    c.append(ele)

print('\nA values:', a, end='')
print('\nB values:', b, end='')
print('\nC values:', c, end='')

# أكتب برنامج يقوم بتعريف ثلاث مصفوفات A و B و C.
# ثم يطلب من المستخدم إدخال عدد يمثل عدد يمثل عدد عناصر المصفوفتين A و B.
# ملاحظة: عدد عناصر المصفوفتين يجب أن يكون أكبر من صفر.
# بعدها يطلب من المستخدم إدخال قيم لجميع عناصر المصفوفتين A و B.
# بعدها يقوم بوضع قيم A و B بنفس الترتيب في المصفوفة C.
# في الأخير, يعرض للمستخدم القيم التي أصبحت تحتويها المصفوفة C.
# Enter the number of A & B elements: 3
# Enter A elements:
# 1
# 2
# 3
# Enter B elements:
# 4
# 5
# 6
# C elements: All A & B values
#
# A values: [1, 2, 3]
# B values: [4, 5, 6]
# C values: [1, 2, 3, 4, 5, 6]
a = []
b = []
n = 0

while n <= 0:
    n = int(input('Enter the number of A & B elements: '))

print('Enter A elements:')
for i in range(0, n):
    ele = int(input())
    a.append(ele)

print('Enter B elements:')
for i in range(0, n):
    ele = int(input())
    b.append(ele)

c = [0] * (2 * n)
print('C elements: All A & B values')
for i in range(0, n):
    c[i] = a[i]
for i in range(0, n):
    c[n + i] = b[i]

print('\nA values:', a, end='')
print('\nB values:', b, end='')
print('\nC values:', c, end='')

# أكتب برنامج يطلب من المستخدم إدخال أي رقم يريد للبحث عنه بداخل مصفوفة أرقام أحادية (ذات بعد واحد) جاهزة.
# بعدها سيقوم البرنامج بطباعة ما إن كانت القيمة موجودة في المصفوفة أم لا.
# ملاحظة: بمجرد أن يتم إيجاد القيمة المراد البحث عنها فإنه يجب إيقاف البحث
# Enter a number: 5
# 5 Is in the array
a = [1, 2, 3, 4, 5, 6]
found = False

n = int(input('Enter a number: '))

for i in range(0, len(a)):
    if a[i] == n:
        found = True
        break

if found:
    print(str(n), 'Is in the array')
else:
    print(str(n), 'Is not in the array')

# أكتب برنامج يطلب من المستخدم إدخال أي رقم يريد للبحث عنه بداخل مصفوفة أرقام أحادية (ذات بعد واحد) جاهزة.
# بعدها سيقوم البرنامج بطباعة كم مرة تم إيجاد الرقم الذي أدخله المستخدم في المصفوفة.
# Enter a number: 6
# 6 Is in the array for 3 times
a = [1, 2, 3, 4, 5, 6, 6, 2, 3, 3, 5, 6, ]
found = False
count = 0

n = int(input('Enter a number: '))

for i in range(0, len(a)):
    if a[i] == n:
        found = True
        count += 1

if found:
    print(str(n), 'Is in the array for', count, 'times')
else:
    print(str(n), 'Is not in the array')

#in6days.