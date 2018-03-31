# -*- coding:utf-8 -*-
answer = 'Banana'

# YES BANANA가 출력되게 하고 싶다.
#differesnce between == and is

if answer is 'Banana':
    print('YES BANANA')

else:
    print('INCORRECT')

# No APPLE. it might be Banana가 출력되게 하고 싶다.
if answer == 'Apple':
    print('YES')
else:
    print('No APPLE. it might be Banana')

# The Best Language is python이 출력되게 하고 싶다.
language = 'python'
text = 'The Best Language is {}'.format(language)
print(text)

# text의 마지막 단어 python을 출력되게 하고 싶다.
words = text.split(' ')
print(words[4])

# 다시 words를 이용해서 The Best Language is python을 만들고 맨 뒤에 줄바꿈 문자를 넣고 싶다.
new_text = ' '.join(words) + '/n'
print(new_text)

# 1부터 10까지 출력하고 싶다.
for i in range(10):
    print(i + 1)

# dictionary인 category에 있는 c를 출력하고 싶다.
category = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
}
print(category.get('4', 'No exist'))

# category에 없는 내용을 조회할 때는 '없어요'가 나오게 하고 싶다.
#print(category.get(4))

search_target = '3'
print(category.get(search_target, "No exist ()". format(search_target)))

