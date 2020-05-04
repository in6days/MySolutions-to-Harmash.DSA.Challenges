#التعامل مع الأرقام و النصوص - التحدي الثاني

# قم بتعريف دالة إسمها RemoveAll, عند استدعاءها نمرر لها نصيّن, فترجع نسخة من النص لا تحتوي على النص الثاني.
# Enter a text: I like cats. I have one cat.
# Enter a word to remove it: cat
# After remove cat from the text: I like s. I have one .
def RemoveAll(s, w):
    return s.replace(w, '')

Text = input('Enter a text: ')
word = input('Enter a word to remove it: ')
result = RemoveAll(Text, word)

print('After remove ' + word + ' from the text: ' + str(result))

# قم بتعريف دالة إسمها ReplaceAll, فكرتها البحث في النص عن جزئية ( كلمة أو جملة ) محددة و تبديلها بجزئية أخرى.
# عند استدعاءها يجب أن نمرر لها ثلاث نصوص. الأول يمثل نص عادي, الثاني يمثل الجزئية التي نريد البحث عنها, و الثالث يمثل الجزئية التي نريد وضعها مكان الجزئية الثانية.
# في النهاية يجب أن ترجع نسخة من النص الأول بعد أن تم تبديل الجزئية التي البحث عنها بالجزئية التي نريد وضعها مكانها.
# Enter a text: "I like cats. I have one cat.
# Enter a word to remove it: cat
# Enter a word to replace it: dog
# Final result: "I like dogs. I have one dog.
def ReplaceAll(s, w1, w2):
    return s.replace(w1, w2)

T = input('Enter a text: ')
w1 = input('Enter a word to remove it: ')
w2 = input('Enter a word to replace it: ')

result = ReplaceAll(T, w1, w2)

print('Final result: ' + str(result))

# قم بتعريف دالة إسمها DoubleChars, نمرر لها نص عند إستدعاءها فتعيد لنا نسخة من هذا النص كل حرف فيها مكرر مرتين.
# Enter a text: Iron Man
# Final result: IIrroonn  MMaann
def DoubleChars(str):
    new_str = ''
    for char in str:
        new_str += char * 2
    return new_str

T = input('Enter a text: ')

result = DoubleChars(T)

print('Final result: ' + str(result))

# قم بإنشاء برنامج يطلب من المستخدم إدخال ثلاث نصوص و يخزنهم في ثلاث متغيرات نصية هي S1, S2 و S3 و بعدها ينفذ التالي:
# يخبره ما إن كان دمج S1 مع S2 يساوي S3 أم لا.
# يخبره ما إن كان S1 يمثل جزء من S2 أو يساويه ( أي S1 == s2 ).
# إذا كان طول S1 أكبر من طول S2 قم بإضافة نص S2 على S1 و خزن الناتج في متغير نصي جديد إسمه S4.
# إذا كان طول S2 أكبر من طول S1 قم بإضافة نص S1 على S2 و خزن الناتج في متغير نصي جديد إسمه S4.
# يخبره ما إن كان S2 يمثل جزء من ثاني نصف في S1.
# يعرض له الأحرف الموجودة في أول نصف في S1.
# Enter text_1: Python
# Enter text_2: on
# Enter text_3: web
# ---------------------
# text_1 + text_2 = text_3.  False
# text_1 is a part of text_2 or text_1 = text_2.  False
# Text_4: on Python
# text_2 is a part of the second half of text_1  True
# The first half of text_1. Pyt
s1 = input('Enter text_1: ')
s2 = input('Enter text_2: ')
s3 = input('Enter text_3: ')
s4 = ''
print('---------------------')

print('text_1 + text_2 = text_3. ', s1 + s2 == s3)

print('text_1 is a part of text_2 or text_1 = text_2. ', s2.find(s1) != -1)

if len(s1) > len(s2):
    s4 = s2 + s1
    print('Text_4: ' + s2 + ' ' + s1)
else:
    s4 = s1 + s2
    print('Text_4: ' + s1 + ' ' + s2)

print('text_2 is a part of the second half of text_1 ', s1[int(len(s1) / 2):].find(s2) != -1)

print('The first half of text_1. ' + s1[0:int(len(s1) / 2)])

# قم بإنشاء برنامج يطلب من المستخدم إدخال نص و من ثم إدخل حرف واحد.
# بعدها سيقوم البرنامج بطباعة مكان كل ( Index ) موجود عليه هذا الحرف في النص
# Enter a text: Harmash is the best site to learn programming
# Enter a character: a
# a found at index: 1
# a found at index: 4
# a found at index: 30
# a found at index: 39
s = input('Enter a text: ')
r = input('Enter a character: ')

for i in range(len(s)-1):
    if s[i]==r:
        print(r+' '+ 'found at index: '+str(i))

#in6days.