import requests
from bs4 import BeautifulSoup

#from 1 to 700

f = open('result.csv', 'w', encoding='utf8')

for inning in range(1, 701):

    url = "http://www.nlotto.co.kr/gameResult.do?method=byWin&drwNo={}".format(inning)

    response = requests.get(url)
    html_doc = response.text

    soup = BeautifulSoup(html_doc, "lxml")
    contents_box = soup.find ('div', {'class': 'lotto_win_number'})
    number_box = contents_box.find('', {'class': 'number'})
    number_images = number_box.find_all('img')

    result = list()
    for tag in number_images:
        temp1 = tag['alt']
        result.append(temp1)

    print(result)
    f.write('{},{},{},{},{},{},{}\n'.format(result[0], result[1], result[2], result[3], result[4], result[5], result[6]
                                          )

            )
f.close()





