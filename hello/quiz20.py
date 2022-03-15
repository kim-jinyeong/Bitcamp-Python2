import urllib
import pandas as pd
import domains
from quiz00 import Quiz00
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Quiz20:

    def quiz20list(self) -> str:
        list = [1, 2, 3, 4]
        print(list)
        print(list[0], list[-1], list[-2], list[1:3])

        list2 = ['math', 'english']
        print(list2[0])

        list3 = [1, '2', [1, 2, 3]]
        print(list3)

        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)

        list4.append(list5)
        print(list4)

        list4[-2:] = []
        print(list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print(c[0][1])

        c[0][1] = 10
        print(c)

        a = range(10)
        print(a)

        print(sum(a))

        b = [2, 10, 0 - 2]
        print(sorted(b))

        print(b.index(0), len(b))

    def quiz21tuple(self) -> str:
        a = (1, 2)
        print(a, type(a))

    def quiz22dict(self) -> str:
        a = {"class": ['deep learning', 'machine learning'], "num_students": [40, 20]}
        print(a)
        print(type(a))
        print(a["class"])
        a['grade'] = ['A', 'B', 'C']
        print(a)
        print(a.keys())
        print(list(a.keys()))
        print(a.values())
        print(a.items())
        print(a.get('class'))
        print('class' in a)

    def quiz23listcom(self) -> str:
        print('-----Legacy-----')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('-----List Comprension-----')
        a2 = [i for i in range(5)]
        print(a2)

        return None

    def quiz24zip(self) -> []:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        #self.find_rank(soup)
        ls1 = self.find_music(soup, 'p', 'class', 'title')
        ls2 = self.find_music(soup, 'p', 'class', 'artist')
        #self.dict2(ls1,ls2)
        #print(dict)
        l = [i + j for i,j in zip(ls1, ls2)]
        l2 = list(zip(ls1,ls2))
        d = {i:j for i,j in zip(ls1, ls2)}
        d1 = dict(zip(ls1,ls2))
        return d
    @staticmethod
    def dict1(ls1,ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict3(ls1,ls2) -> None:
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)

    @staticmethod
    def print_music_list(soup):
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self,soup):
        topic = ['artist', 'title']
        for i,j in enumerate(self.find_music( soup, 'p', 'class', topic)):
            print(f'{i} 위 : {j}')

    @staticmethod
    def find_music(soup, tag, tp, name) -> []:
        ls = soup.find_all(tag, {tp : name})
        return [i.get_text().strip() for i in ls]

    @staticmethod
    def quiz25dictcom() -> None:
        students = []
        scores = []
        [scores.append(domains.myRandom(0, 100)) for i in range(5)]
        while(1):
            students = set(students)
            students.add(Quiz00.quiz06memberChoice())
            if len(students) == 5:break
        d = dict(zip(students,scores))
        df = pd.DataFrame.from_dict(d, orient = 'index')
        print(type(d))
        print(df)
        return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> []:
        headers = {'User-Agent': 'Mozilla/5.0' }
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030815'
        req = urllib.request.Request(url, headers= headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        ls1 = self.find_music(soup,'div', 'class', 'ellipsis rank01')
        ls2 = self.find_music(soup,'span', 'class', 'checkEllipsis')
        dict = {}

        for i, j in zip(ls1, ls2):
            dict[i] = j
        return dict

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient = 'index')
        print(df)
        df.to_csv('./save/bugs.csv', sep = ',' , na_rep = 'NaN')

    def quiz29_pandas_df(self) -> None:
        num1 = []
        num2 = []
        col = [chr(i) for i in range(97,100)]
        [num2.append(i) if i % 2 == 0 else num1.append(i) for i in range(1,7)]
        d1 = {"1": num1, "2": num2}
        df = pd.DataFrame.from_dict(d1, orient = 'index', columns = col)
        print(df)
        return None
