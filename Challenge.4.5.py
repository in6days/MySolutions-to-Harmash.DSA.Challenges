#التعامل مع المصفوفات - التحدي الخامس

# أكتب برنامج يطلب من المستخدم إدخال أي رقم يريد للبحث عنه بداخل مصفوفة أرقام ثنائية (ذات بعدين) جاهزة.
# بعدها سيقوم البرنامج بطباعة ما إن كانت القيمة موجودة في المصفوفة أم لا.
# ملاحظة: أوقف عملية البحث بمجرد إيجاد عنصر يملك نفس القيمة المراد البحث عنها
# Enter a number: 4
# 4 is in the matrix
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

found = False

n = int(input('Enter a number: '))

for i in range(len(m)):
    for j in range(len(m[i])):

        if m[i][j] == n:
            found = True
            break

if found:
    print(str(n), 'is in the matrix', end='')
else:
    print(str(n), 'is not in the matrix')

# أكتب برنامج يطلب من المستخدم إدخال أي رقم يريد للبحث عنه بداخل مصفوفة أرقام ثنائية (ذات بعدين) جاهزة.
# # بعدها سيقوم البرنامج بطباعة كم مرة تم إيجاد الرقم الذي أدخله المستخدم في المصفوفة.
# Enter a number: 6
# 6 is in the matrix: 3 time(s)
m = [
    [6, 2, 3],
    [4, 3, 6],
    [7, 6, 9]
]

found = False
count = 0

n = int(input('Enter a number: '))

for i in range(len(m)):
    for j in range(len(m[i])):

        if m[i][j] == n:
            found = True
            count += 1

if found:
    print(str(n), 'is in the matrix:', str(count), 'time(s)', end='')
else:
    print(str(n), 'is not in the matrix')

# أكتب برنامج يقوم بترتيب جميع القيم الموجودة في مصفوفة أرقام ثنائية جاهزة من الأصغر إلى الأكبر.
# قم بعرض القيم الموجودة في المصفوفة قبل الترتيب و بعد الترتيب.
# Matrix before sorting
# 2 8 9
# 4 1 6
# 7 5 3
# Matrix AFTER sorting
# 1 2 3
# 4 5 6
# 7 8 9
matrix = [
    [2, 8, 9],
    [4, 1, 6],
    [7, 5, 3]
]

rows = len(matrix)
cols = len(matrix[0])
array = [0] * (rows * cols)

print('Matrix before sorting ')
for i in range(rows):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
    print()

for i in range(rows):
    for j in range(cols):
        array[j + (i * rows)] = matrix[i][j]

for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
        if array[j] < array[i]:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = array[j + (i * rows)]

print('\nMatrix AFTER sorting ')
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()

# أكتب برنامج يطلب من المستخدم إعطائه عددين, العدد الأول يمثل عدد أسطر مصفوفة ثنائية ( ذات بعدين ) إسمها matrix و العدد الثاني يمثل عدد أعمدتها.
# ملاحظة: عدد أسطر و أعمدة المصفوفة يجب أن يكون أكبر من صفر.
# بعدها يطلب من المستخدم إدخال عدد صحيح لكل عنصر فيها.
# في الأخير يعرض للمستخدم عدد العناصر التي تملك قيم أكبر من صفر, و عدد العناصر التي تملك قيم أصغر من صفر, و عدد العناصر التي تملك قيم تساوي صفر.
# Enter number of rows: 3
# Enter number of columns: 2
# Enter matrix[0][0]: 5
# Enter matrix[0][1]: -5
# Enter matrix[1][0]: -7
# Enter matrix[1][1]: 0
# Enter matrix[2][0]: 8
# Enter matrix[2][1]: 1
# matrix values
# 5 -5
# -7 0
# 8 1
# Number of negative elements: 2
# Number of 0: 1
# Number of positive elements: 3
rows, cols = (0, 0)
pos_count = 0
neg_count = 0
zero_count = 0

while rows <= 0:
    rows = int(input('Enter number of rows: '))
while cols <= 0:
    cols = int(input('Enter number of columns: '))

matrix = [[0] * cols for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input('Enter matrix[' + str(i) + '][' + str(j) + ']: '))

print('\nmatrix values')
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] < 0:
            neg_count += 1
        elif matrix[i][j] > 0:
            pos_count += 1
        else:
            zero_count += 1

print('Number of negative elements:', neg_count, end='')
print('\nNumber of 0:', zero_count, end='')
print('\nNumber of positive elements:', pos_count, end='')

# أكتب برنامج يعرّف مصفوفة مربعة إسمها matrix تتألف من 3 أسطر و 3 أعمدة.
# ثم يطلب من المستخدم إدخال قيم لها.
# إنتبه: نريد هذه المصفوفة أن تحتوي فقط على قيم أكبر أو تساوي صفر.
# ثم يعرض للمستخدم جميع القيم التي أصبحت تحتويها المصفوفة.
# بعدها يقوم بجمع قيم جميع العناصر الموجودة على القطر ( On Diagonal ), فوق القطر ( Above Diagonal ), و تحت القطر ( Under Diagonal ).
# في الأخير يعرض للمستخدم ناتج الجمع
# Enter matrix[0][0]: 1
# Enter matrix[0][1]: 2
# Enter matrix[0][2]: 3
# Enter matrix[1][0]: 4
# Enter matrix[1][1]: 5
# Enter matrix[1][2]: 6
# Enter matrix[2][0]: 7
# Enter matrix[2][1]: 8
# Enter matrix[2][2]: 9
# matrix values
# 1 2 3
# 4 5 6
# 7 8 9
# Sum of values above diagonals: 11
# Sum of values under diagonals: 19
# Sum of values on diagonals: 15
rows, cols = (3, 3)
matrix = [[0] * cols for i in range(rows)]
sum_on_diagonals = 0
sum_above_diagonals = 0
sum_under_diagonals = 0

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input("Enter matrix[" + str(i) + "][" + str(j) + "]: "))

print('\nmatrix values')
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()

for i in range(rows):
    for j in range(cols):
        if j > i:
            sum_above_diagonals += matrix[i][j]
        elif j < i:
            sum_under_diagonals += matrix[i][j]
        else:
            sum_on_diagonals += matrix[i][j]

print('\nSum of values above diagonals:', sum_above_diagonals)
print('Sum of values under diagonals:', sum_under_diagonals)
print('Sum of values on diagonals:', sum_on_diagonals)

#in6days.