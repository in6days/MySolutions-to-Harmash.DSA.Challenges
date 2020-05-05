#التعامل مع الأرقام و النصوص - التحدي الثالث

# قم بتعريف دالة إسمها CountWords, عند استدعاءها نمرر لها نص, فترجع عدد الكلمات الموجودة في هذا النص.
# Enter a text: Programming is easy to learn.
# The number of words is: 5
def CountWords(str):
    return len(str.split())


s = input('Enter a text: ')

result = CountWords(s)

print('The number of words is: ' + str(result))

# قم بتعريف دالة إسمها CountNoneEscapeChars, عند استدعاءها نمرر لها نص, فترجع عدد الأحرف الموجودة في هذا النص.
# ملاحظة: أي حرف يعتبر Escape Character مثل الأحرف \t و \n إلخ.. لا يجب أن يتم حساب عددهم ضمن عدد الأحرف.
# يمكنك إستخدام الـ Regex إن أردت للتمييز بين الأحرف العادية و الأحرف التي تعتبر Escape Characters.
# t = "Hi Lora.\nHow are you?."
# The Count withot Escap Chars is: 18

import re

def CountNoneEscapeChars(txt):
    count = 0
    for char in txt:
        if re.match('\S', char):
            count += 1

    return count

t = "Hi Lora.\nHow are you?."

result = CountNoneEscapeChars(t)

print('The Count withot Escap Chars is:', result)

# قم بتعريف دالة إسمها PrintWordsOccurence, نمرر لها نص عند إستدعاءها فتقوم بطباعة كم مرة تكررت كل كلمة في هذا النص.
# Text: I am happy. I am a doctor. I like chocolate.
# Words Occurence:  {'I': 3, 'am': 2, 'happy.': 1, 'a': 1, 'doctor.': 1, 'like': 1, 'chocolate.': 1}
def PrintWordsOccurence(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

txt = input('Text: ')

result = PrintWordsOccurence(txt)

print('Words Occurrence: ', result)

# قم بإنشاء برنامج يطلب من المستخدم إدخال نصّين, بعدها يقوم بطباعة ما إن كان النص الأول يبدأ بالنص الثاني أم لا.
# Enter text 1: I like programming.
# Enter text 2: Hello
# --------------------------------
# Text 1 NOT starts with Hello
t1 = input('Enter text 1: ')
t2 = input('Enter text 2: ')

same = True
i =0

while i<len(t2) and same:
    if t1[i] != t2[i]:
        same = False
    i += 1
print('--------------------------------')

if same:
    print('Text 1 starts with '+t2)
else:
    print('Text 1 NOT starts with '+t2)

# قم بإنشاء برنامج يطلب من المستخدم إدخال نصّين, بعدها يقوم بطباعة ما إن كان النص الأول ينتهي بالنص الثاني أم لا.
# t1 = input('Enter text 1: ')
# t2 = input('Enter text 2: ')

t2_counter = 0
same = True
i = len(t1) - len(t2)

while i < len(t1) and same:
    if t1[i] != t2[t2_counter]:
        same = False
    t2_counter += 1
    i += 1

print('--------------------------------')

if same:
    print('Text 1 end with ' + t2)
else:
    print('Text 1 NOT end with ' + t2)

#in6days.




