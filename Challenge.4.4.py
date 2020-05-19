#التعامل مع المصفوفات - التحدي الرابع

# أكتب برنامج يطلب من المستخدم إعطائه عددين, العدد الأول يمثل عدد أسطر مصفوفة ثنائية ( ذات بعدين ) إسمها matrix و العدد الثاني يمثل عدد أعمدتها.
# ملاحظة: عدد أسطر و أعمدة المصفوفة يجب أن يكون أكبر من صفر.
# بعدها يطلب من المستخدم إدخال عدد صحيح لكل عنصر فيها.
# في الأخير, سيعرض للمستخدم جميع القيم المخزنة فيها بشكل مرتب.
# Enter rows number: 2
# Enter columns number: 3
# Enter matrix[0][0]: 2
# Enter matrix[0][1]: 3
# Enter matrix[0][2]: 5
# Enter matrix[1][0]: 7
# Enter matrix[1][1]: 11
# Enter matrix[1][2]: 13
# matrix values
# 2 3 5
# 7 11 13
rows = 0
cols = 0

while rows <= 0:
    rows = int(input('Enter rows number: '))
while cols <= 0:
    cols = int(input('Enter columns number: '))

matrix = [[0] * cols for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input('Enter matrix[' + str(i) + '][' + str(j) + ']: '))

print('\nmatrix values')
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()

#أكتب برنامج يعرّف مصفوفة إسمها matrix تتألف من 3 أسطر و 3 أعمدة.
#
بعدها يطلب من المستخدم إدخال عدد صحيح لكل عنصر فيها.
# في الأخير, يعرض للمستخدم ناتج جمع جميع قيم عناصرها
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
# Sum of all values: 45
rows, cols = (3, 3)
sum = 0
matrix = [[0] * cols for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input('Enter matrix[' + str(i) + '][' + str(j) + ']: '))

print('\nmatrix values')
for i in range(rows):
    for j in range(cols):
        sum += matrix[i][j]
        print(matrix[i][j], end=' ')
    print()

print('\nSum of all values:', sum, end='')

# أكتب برنامج يعرّف مصفوفة إسمها matrix تتألف من 3 أسطر و 3 أعمدة.
# بعدها يطلب من المستخدم إدخال عدد صحيح لكل عنصر فيها.
# في الأخير, يعرض للمستخدم ناتج جمع قيم العناصر الموجودة في كل سطر فيها.
# Enter matrix[0][0]: 1
# Enter matrix[0][1]: 2
# Enter matrix[0][2]: 3
# Enter matrix[1][0]: 4
# Enter matrix[1][1]: 5
# Enter matrix[1][2]: 6
# Enter matrix[2][0]: 7
# Enter matrix[2][1]: 8
# Enter matrix[2][2]: 9
# -------------------
# The sum in row 0 is: 6
# The sum in row 1 is: 15
# The sum in row 2 is: 24
rows, cols =(3, 3)
matrix = [[0] * cols for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input('Enter matrix[' + str(i) + '][' + str(j) + ']: '))

print('-------------------')
for i in range(rows):
    sumRow = 0
    for j in range(cols):
        sumRow += matrix[i][j]
    print('The sum in row '+str(i)+' is:', sumRow)

# أكتب برنامج يعرّف مصفوفة إسمها matrix تتألف من 3 أسطر و 3 أعمدة.
# بعدها يطلب من المستخدم إدخال عدد صحيح لكل عنصر فيها.
# في الأخير, يعرض للمستخدم ناتج جمع قيم العناصر الموجودة في كل عامود فيها.
# Enter matrix[0][0]: 1
# Enter matrix[0][1]: 2
# Enter matrix[0][2]: 3
# Enter matrix[1][0]: 4
# Enter matrix[1][1]: 5
# Enter matrix[1][2]: 6
# Enter matrix[2][0]: 7
# Enter matrix[2][1]: 8
# Enter matrix[2][2]: 9
# -------------------
# The sum in column 0 is: 12
# The sum in column 1 is: 15
# The sum in column 2 is: 18
rows, cols =(3, 3)
matrix = [[0] * cols for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input('Enter matrix[' + str(i) + '][' + str(j) + ']: '))

print('-------------------')
for i in range(rows):
    sumCol =0
    for j in range(cols):
        sumCol += matrix[j][i]
    print('The sum in column '+str(i)+' is:', sumCol)

# أكتب برنامج يعرّف مصفوفة إسمها matrix تتألف من 3 أسطر و 3 أعمدة.
# بعدها يطلب من المستخدم إدخال عدد صحيح لكل عنصر فيها.
# بعدها يعرض للمستخدم جميع القيم التي أصبحت تحتويها بشكل مرتب.
# بعدها يقوم بتخزين جميع القيم الموجودة في المصفوفة matrix بداخل مصفوفة أحادية ( ذات بعد واحد ) إسمها array.
# في الأخير, يعرض للمستخدم جميع القيم التي أصبحت تحتويهم المصفوفة array على سطر واحد مع وضع مسافة فارغة بين كل قيمتين
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
# Array values
# 1 2 3 4 5 6 7 8 9
rows, cols = (3, 3)
matrix = [[0] * cols for i in range(rows)]
array = [0] * rows * cols

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
        array[j + (i * rows)] = matrix[i][j]

print('\nArray values')
for i in range(len(array)):
    print(array[i], end=' ')

#in6days.