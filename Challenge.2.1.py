#التعامل مع الأرقام و النصوص - التحدي الأول

# أكتب برنامج يطلب من المستخدم إدخال رقم. بعدها يعرض له ناتج جمع أعداد هذا الرقم.
sum = 0
n = int(input('Enter a number: '))

while n != 0:
    sum += n%10
    n = int(n/10)
print('The sum of its digits is: '+ str(sum))

#أكتب برنامج يطلب من المستخدم إدخال رقم. بعدها يعرض له نسخة من هذا الرقم و لكن بشكل معكوس.
rev = 0
n = int(input('Enter a number: '))

while n!=0:
    remainder = n%10
    rev = rev*10 + remainder
    n = int(n/10)
print('Its reverse is: '+ str(rev))

# أكتب برنامج يطلب من المستخدم إدخال رقم. بعدها يعرض له إن كان هذا الرقم عبارة عن Palindrome أم لا.
# الـ Palindrome عبارة عن رقم أعداده معكوسة بشكل متساوي من اليمين إلى اليسار و من اليسار إلى اليمين.
#n = int(input('Enter a number: '))

rev = 0
origin_n = n

while n != 0:
    remainder = n % 10
    rev = rev * 10 + remainder
    n = int(n / 10)

if origin_n == rev:
    print(str(origin_n) + ' is a Palindrome')

else:
    print(str(origin_n) + ' is Not a Palindrome')

#قم بتعريف دالة إسمها CountOccurrences, عند استدعاءها نمرر لها نصيّن, فترجع عدد صحيح يمثل كم مرة النص الثاني مكرر في النص الأول.
# بعدها قم بتجربة هذه الدالة في البرنامج مع جعل المستخدم هو من يدخل النصيّن.
# Enter a text:  I like cats. I have one cat called Lola
# Enter word to search occurrences: cat
# Count occurrences of cat is: 2
def CountOccurrences(s, w):
    count = 0
    for i in range(0, len(s)-len(w) +1):
        if s[i:i+len(w)]== w:
            count += 1
    return count

Text = input('Enter a text: ')
word = input('Enter word to search occurrences: ')
result = CountOccurrences(Text, word)

print('Count occurrences of '+word+ ' is: '+str(result))

# قم بتعريف دالة إسمها ReverseString, عند استدعاءها نمرر لها نص, فترجعه معكوساً.
# بعدها قم بتجربة هذه الدالة في البرنامج مع جعل المستخدم هو يدخل النص الذي سيتم عرضه بشكل عكس
# Enter a text: I love programming
# The reverse string is: gnimmargorp evol I
def ReverseString(s):
    return s[::-1]

Text = input('Enter a text: ')
result = ReverseString(Text)

print('The reverse string is: '+str(result))

#in6days.
