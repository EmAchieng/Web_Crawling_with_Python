import random
from pprint import pprint

#기초자료 \가 import dates

f = open('result.csv', 'r', encoding='utf8')

texts = f.readable()
raw_data = dict()

 #for test in texts:
     #text =' 10, 23, 25, 34, 36, 40\n'
for index, one_line in enumerate(texts):

    text = one_line.replace('\n', "")
    numbers = text.split(',')
    raw_data['{}회'.format(index + 1)] = numbers

    pass

result = dict()

#initialize result data
for i in range(1, 46):
    result[str(i)] = 0

index_list = raw_data.keys()

for index in index_list:
    numbers = raw_data[index]

    for num in numbers:
        result[num] = result[num] + 1


"""
1 - 2, 1- 3, 1- 4... every combination
"""



result2 = dict()
for i in range(1, 46):
    for j in range(i+1, 46):
        combination_name = '{}--{}'.format(i, j)
        result2[combination_name] = 0



    for index in index_list:
        numbers = raw_data[index]
        numbers = numbers[:-1]

        for i in numbers: # 6 numbers
            now_index = numbers.index(i)
            for j in numbers[now_index + 1:]:
                print('{}--{}'.format(i, j))
                combination_name = '{}--{}'.format(i, j)
                result2[combination_name] = result2[combination_name] + 1
"""
random number generate
"""


candidate_list = list()
for i in random(10000):

    temp = random.sample(range(1, 46), 6)
    temp.sort()
    candidate_list.append(temp)


#evaluate each candidate

evaluated_list = list()

for candidate in candidate_list:
    score = 0
    for i in candidate:  # 6 numbers
        now_index = numbers.index(i)
        for j in numbers[now_index + 1:]:
            print('{}--{}'.format(i, j))
            combination_name = '{}--{}'.format(i, j)
            score = score + result2[combination_name]
    evaluated_list.append((score, candidate))

pass


#result (evaluated_list) sorting


evaluated_list.sort(reverse=True)

top10 = evaluated_list[:10]

pprint(top10)










