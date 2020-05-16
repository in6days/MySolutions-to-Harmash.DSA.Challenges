#التعامل مع المصفوفات - التحدي الأول

# أكتب برنامج يطلب من المستخدم إعطائه عدد يمثل عدد عناصر مصفوفة إسمها arr و يخزنه في متغير إسمه n.
# ملاحظة: عدد عناصر المصفوفة يجب أن يكون أكبر من صفر.
# بعدها ينشئ المصفوفة arr و يحدد أن عدد عناصرها هو العدد الذي أدخله المستخدم.
# بعدها يطلب من المستخدم إدخال عدد صحيح لكل عنصر فيها.
# في الأخير, سيعرض للمستخدم عدد عناصر المصفوفة, يليه جميع القيم المخزنة فيها على سطر واحد مع وضع فاصلة بين كل قيمتين.
# Enter number of array elements: 4
# Enter the elements:
# 2
# 3
# 5
# 7
# Array value: [2, 3, 5, 7]
arr = []
n=0
while n<=0:
    n = int(input('Enter number of array elements: '))
print('Enter the elements:')
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print('Array value:', arr, end='')

# في الأخير, سيعرض للمستخدم ناتج جمع جميع قيم عناصر المصفوفة.
# Enter number of array elements: 4
# Enter the elements:
# 1
# 2
# 3
# 4
# Array value: [1, 2, 3, 4]
# Sum of values: 10
arr = []
n=0
sum=0
while n<=0:
    n = int(input('Enter number of array elements: '))
print('Enter the elements:')
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
    sum += ele
print('Array value:', arr, '\nSum of values:', sum, end='')

# في الأخير يعرض للمستخدم عدد العناصر التي تملك قيم أكبر من صفر, و عدد العناصر التي تملك قيم أصغر من صفر, و عدد العناصر التي تملك قيم تساوي صفر.
# Enter number of array elements: 6
# Enter the elements:
# -2
# -1
# 0
# 1
# 2
# 3
# Number of negative elements: 2
# Number of 0: 1
# Number of positive elements: 3
arr = []
n = 0
pos_count = 0
neg_count = 0
zero_count = 0

while n <= 0:
    n = int(input('Enter number of array elements: '))
print('Enter the elements:')
for i in range(0, n):
    ele = int(input())
    arr.append(ele)

for num in arr:
    if num < 0:
        neg_count += 1
    elif num > 0:
        pos_count += 1
    else:
        zero_count += 1

print('Number of negative elements:', neg_count, end='')
print('\nNumber of 0:', zero_count, end='')
print('\nNumber of positive elements:', pos_count, end='')

# في الأخير, يقوم بترتيب قيم عناصر المصفوفة من الأصغر إلى الأكبر و من ثم يعرضها له من جديد.
# Enter number of array elements: 4
# Enter the elements:
# 2
# 3
# 5
# 7
# Array value: [2, 3, 5, 7]
# Array sort: [2, 3, 5, 7]
arr = []
n=0
while n<=0:
    n = int(input('Enter number of array elements: '))
print('Enter the elements:')
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print('Array value:', arr, end='')
arr.sort()
print('\nArray sort:',arr , end='')

# في الأخير, يقوم بترتيب قيم عناصر المصفوفة من الأكبر إلى الأصغر و من ثم يعرضها له من جديد.
# Enter number of array elements: 4
# Enter the elements:
# 2
# 3
# 5
# 7
# Array value: [2, 3, 5, 7]
# Array sort: [7, 5, 3, 2]
# Entrée [ ]:
arr = []
n=0
while n<=0:
    n = int(input('Enter number of array elements: '))
print('Enter the elements:')
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print('Array value:', arr, end='')
arr.sort(reverse=True)
print('\nArray sort:',arr , end='')

#in6days.