#التعامل مع المصفوفات - التحدي الثالث

# قم بتعريف دالة إسمها FindAll,
# مهمتها البحث في مصفوفة أحادية ( تتألف من أعداد صحيحة ) نمررها لها عن قيمة محددة أيضاً نمررها لها, و من ثم طباعة Index كل عنصر يملك هذه القيمة.
# بعدها قم بتجربة هذه الدالة في البرنامج.
# مثال:إذا قمنا باستدعاء الدالة FindAll() و تمرير المصفوفة 1, 2, 3, 2, 5, 2, 7, 2 و القيمة 2 لها فستكون نتيجة البحث كالتالي
# 2 Found at index: 1
# 2 Found at index: 3
# 2 Found at index: 5
# 2 Found at index: 7
arr=[]

def FindAll(arr, e):
    for i in range(0, len(arr)):
        if arr[i]==e:
            print(str(e)+' Found at index: '+str(i))

arr = [1, 2, 3, 2, 5, 2, 7, 2]
e = 2

FindAll(arr, e)

# قم بتعريف دالة إسمها CountOccurrence, 
# مهمتها البحث في مصفوفة أحادية ( تتألف من أعداد صحيحة ) و طباعة كم مرة تكررت كل قيمة موجودة فيها.
# The count of 0 is: 2
# The count of 4 is: 3
# The count of 2 is: 4
# The count of 3 is: 2
# The count of 5 is: 1
# The count of 1 is: 1
def CountOccurrence(arr):
    for i in range(0, len(arr)):
        count = 1
        if arr[i] is not None:
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    count += 1
                    arr[j] = None

            print('The count of ' + str(arr[i]) + ' is:', str(count))


arr = [0, 4, 2, 3, 2, 4, 3, 5, 2, 0, 1, 4, 2]

CountOccurrence(arr)

# أكتب برنامج يطلب من المستخدم إعطائه عدد يمثل عدد عناصر مصفوفة إسمها arr 
# و يخزنه في متغير إسمه n.
# ملاحظة: عدد عناصر المصفوفة يجب أن يكون أكبر من صفر.
# بعدها ينشئ المصفوفة arr و يحدد أن عدد عناصرها هو العدد الذي أدخله المستخدم.
# بعدها يطلب من المستخدم إدخال عدد صحيح لكل عنصر فيها.
# بعدها يعرض للمستخدم جميع القيم التي أدخلها بنفس الترتيب.
# في الأخير يقوم بترتيب جميع القيم بشكل عكسي ( مثلاً القيمة الأخيرة تصبح في الأول ) و من ثم يعرض قيم المصفوفة من جديد.
# Enter number of array elements: 4
# Enter the elements:
# 7
# 2
# 8
# 6
# Array value: [7, 2, 8, 6]
# Array sort backward: [6, 8, 2, 7]
arr = []
n = 0
while n <= 0:
    n = int(input('Enter number of array elements: '))
print('Enter the elements:')
for i in range(0, n):
    ele = int(input())
    arr.append(ele)

print('Array value:', arr, end='')

for i in range(0, int(n / 2)):
    temp = arr[i]
    arr[i] = arr[n - 1 - i]
    arr[n - 1 - i] = temp

print('\nArray sort backward:', arr, end='')

# أكتب برنامج يطلب من المستخدم إعطائه عدد يمثل عدد عناصر مصفوفة إسمها arr
# و يخزنه في متغير إسمه n.
# ملاحظة: عدد عناصر المصفوفة يجب أن يكون أكبر من صفر.
# بعدها ينشئ المصفوفة arr و يحدد أن عدد عناصرها هو العدد الذي أدخله المستخدم.
# بعدها يطلب من المستخدم إدخال عدد لكل عنصر فيها.
# في الأخير, يعرض للمستخدم متوسط هذه القيم
# Enter number of array elements: 3
# Enter the elements:
# 2
# 1
# 5
# Array value: [2, 1, 5]
# Average of all values: 2.6666666666666665
arr = []
n = 0
sum = 0

while n <= 0:
    n = int(input('Enter number of array elements: '))
print('Enter the elements:')
for i in range(0, n):
    ele = int(input())
    arr.append(ele)

print('Array value:', arr, end='')

for i in range(0, n):
    sum += arr[i]

print('\nAverage of all values:', sum / n, end='')

# أكتب برنامج يطلب من المستخدم إدخال علامة لكل مادة من مواد قم بتجهيز أسماءها في مصفوفة إسمها methods.
# العلامات التي يدخلها المستخدم يجب تخزينها في مصفوفة ثانية مع الإشارة إلى أن العلامة يمكن أن تكون بين 0 و20 فقط.
# بعدها قم بحساب متوسط العلامات التي أدخلها المستخدم.
# في الأخير, إعرض للمستخدم متوسط العلامات التي أدخلها و عبارة ناجح إذا كان معدله أكبر أو يساوي 10 و عبارة راسب إن كان أقل
# Enter Maths note: 15
# Enter Physic note: 10
# Enter History note: 12
# Enter English note: 7
# Average: 11.0 [ Succeeded ]
methods = ['Maths', 'Physic', 'History', 'English']
total_methods = len(methods)
notes = [-1] * len(methods)
avg = 0

for i in range(0, total_methods):
    while notes[i] < 0 or notes[i] > 20:
        notes[i] = int(input('Enter ' + methods[i] + ' note: '))

for i in range(0, total_methods):
    avg += notes[i]
avg /= total_methods
print('\nAverage:', avg, end=' ')

if avg >= 10:
    print('[ Succeeded ]')
else:
    print('[ Failed ]')
    
#in6days.
