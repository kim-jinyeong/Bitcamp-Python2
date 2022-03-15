import random
from domains import myRandom

class Quiz10:

    def quiz10bubble(self) -> str:
        arr = []
        for i in range(0,10):
            arr.append(myRandom(0, 100))
        print(f'랜덤으로 생성된 배열 \n{arr}')
        for i in range(0, len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = temp
        print(f'버블정렬된 배열 \n{arr}')
    def quiz11insertion(self) -> str: return None

    def quiz12selection(self) -> str: return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

    def quiz17prime(self) -> str: return None

    def quiz18golf(self) -> str: return None

    def quiz19booking(self) -> str: return None