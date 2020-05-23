#التعامل مع المصفوفات - التحدي السادس

# قم بتعريف دالة إسمها PrintSecondBiggest,
#عند استدعاءها نمرر لها مصفوفة أحادية (ذات بعد واحد) فتقوم بطباعة ثاني أكبر عدد موجود فيها.
# بعدها قم بإنشاء مصفوفة في البرنامج و تجربة استدعاء الدالة لمعرفة ثاني أكبر عدد موجود في المصفوفة.
# arr=[4, 15, 7, 20, 12, 105, 105, 104, 7]
# The second biggest value is: 104
def PrintSecondBiggest(arr):
    new_arr = set(arr)
    new_arr.remove(max(new_arr))
    print('The second biggest value is:', max(new_arr))

arr = [4, 15, 7, 20, 12, 105, 105, 104, 7]

PrintSecondBiggest(arr)

# قم بتعريف دالة إسمها PrintSecondLowest,
#عند استدعاءها نمرر لها مصفوفة أحادية (ذات بعد واحد) فتقوم بطباعة ثاني أصغر عدد موجود فيها.
# بعدها قم بإنشاء مصفوفة في البرنامج و تجربة استدعاء الدالة لمعرفة ثاني أصغر عدد موجود في المصفوفة.
# arr=[3, 4, 4, 15, 7, 20, 12, 105, 3, 105, 104, 7]
# The second lowest value is: 4
def PrintSecondLowest(arr):
    new_arr = set(arr)
    new_arr.remove(min(new_arr))
    print('The second lowest value is:', min(new_arr))

arr = [3, 4, 4, 15, 7, 20, 12, 105, 3, 105, 104, 7]

PrintSecondLowest(arr)

# أكتب برنامج يطلب من المستخدم إعطائه عدد يمثل عدد عناصر مصفوفة إسمها arr و يخزنه في متغير إسمه n.
# ملاحظة: عدد عناصر المصفوفة يجب أن يكون أكبر من صفر.
# بعدها ينشئ المصفوفة arr و يحدد أن عدد عناصرها هو العدد الذي أدخله المستخدم.
# بعدها يقوم بإعطاء قيمة عشوائية بين 1 و 10 لكل عنصر فيها.
# في الأخير, سيعرض للمستخدم جميع القيم المخزنة فيها على سطر واحد مع وضع فاصلة بين كل قيمتين و من ثم ناتج جمع جميع العناصر
# Enter number of array elements: 6
# Array elements: 2, 2, 5, 1, 7, 8
# Sum of all elements: 25
import random

n = 0
sum = 0
while n <= 0:
    n = int(input('Enter number of array elements: '))

arr = [0] * n

for i in range(n):
    arr[i] = random.randint(1, 10)
print('\nArray elements:', end=' ')

for i in range(n):
    print(arr[i], end='')
    if i < n - 1:
        print(', ', end='')

for i in range(n):
    sum += arr[i]
print("\nSum of all elements:", sum)

# قم بتعريف دالة إسمها PrintLongestName, 
#عند استدعاءها نمرر لها مصفوفة تحتوي على أسماء أشخاص فتقوم بطباعة الإسم الأطول و عدد أحرفه.
# بعدها قم بإنشاء مصفوفة أسماء في البرنامج و تجربة استدعاء الدالة لمعرفة ما هو الإسم الأطول الموجود في المصفوفة
# arr=['Monday', 'Mathematics', 'Physic', 'English', 'Programming', 'Python']
# The longest name is: Programming
# Its length: 11
def PrintLongestName(arr):
    sortedarr = sorted(arr, key=len)
    print('The longest name is:', sortedarr[-1], '\nIts length:', len(sortedarr[-1]))

arr=['Monday', 'Mathematics', 'Physic', 'English', 'Programming', 'Python']

PrintLongestName(arr)

# قم بتعريف دالة إسمها CompareArrays,
#عند استدعاءها نمرر لها مصفوفتين أحاديتين (عندهم بعد واحد) يحتويان على أعداد صحيحة فتقوم بمقارنتهما
# و من ثم طباعة ما إن كانتا متطابقتين من حيث عدد العناصر و قيمهم أم لا.
# بعدها قم بإنشاء مصفوفتين أو أكثر في البرنامج و تجربة استدعاء الدالة لمعرفة ما إن كان يوجد بينهم تطابق أم لا
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [1, 2, 3, 4, 5]
# arr3 = [1, 2, 3, 6, 8]
# arr4 = [1, 2, 3, 4]
# arr5 = arr=['Monday', 'Mathematics', 'Physic', 'English', 'Programming']
# Compare arr1 & arr2: They have the same length and their values are equal
# Compare arr1 & arr3: They have the same length but their values are not equals
# Compare arr1 & arr4: They have different lengths
# Compare arr1 & arr5: They have the same length but their values are not equals
# Compare arr3 & arr5: They have the same length but their values are not equals
# Compare arr4 & arr5: They have different lengths
def compareArrays(arr1, arr2):
    if len(arr1) == len(arr2):
        print('They have the same length', end='')
    else:
        print('They have different lengths')
        return
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            print(' but their values are not equals')
            return
    print(' and their values are equal')


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]
arr3 = [1, 2, 3, 6, 8]
arr4 = [1, 2, 3, 4]
arr5 = arr = ['Monday', 'Mathematics', 'Physic', 'English', 'Programming']

print('Compare arr1 & arr2:', end=' ')
compareArrays(arr1, arr2)
print('Compare arr1 & arr3:', end=' ')
compareArrays(arr1, arr3)
print('Compare arr1 & arr4:', end=' ')
compareArrays(arr1, arr4)
print('Compare arr1 & arr5:', end=' ')
compareArrays(arr1, arr5)
print('Compare arr3 & arr5:', end=' ')
compareArrays(arr3, arr5)
print('Compare arr4 & arr5:', end=' ')
compareArrays(arr4, arr5)

#in6days.
