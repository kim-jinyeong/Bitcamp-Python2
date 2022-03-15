import random
from shlex import join

from domains import my100, myRandom, Member, memberlist


class Quiz00:
    def quiz00calculator(self)->float:
        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        o2 = o[myRandom(0, 4)]
        res = ''
        if o2 == '+':
            res = f'{a} {o2} {b} = {self.add(a, b)}'
        elif o2 == '-':
            res = f'{a} {o2} {b} = {self.sub(a, b)}'
        elif o2 == '*':
            res = f'{a} {o2} {b} = {self.mul(a, b)}'
        elif o2 == '/':
            res = f'{a} {o2} {b} = {self.div(a, b)}'
        elif o2 == '%':
            res = f'{a} {o2} {b} = {self.mod(a, b)}'
        print(res)
        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = '홍길동'
        this.height = 170.8
        this.weight = 120.8
        res = this.weight / (this.height * this.height) * 10000
        if res > 25:
            res = '비만'
        elif res > 23:
            res = '과체중'
        elif res > 18.5:
            res = '정상'
        else:
            res = '저체중'
        print(res)
    def quiz02dice(self):
        print(myRandom(1, 6))

    def quiz03rps(self):
        com = myRandom(1, 3)
        user = myRandom(1, 3)
        rps = ['바위', '가위', '보']
        res = ''
        if user == 1 or user == 2:
            res = f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Draw" if (user == com) else f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Win" \
                if (user > (com + 1) % 3) else f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Lose"
        elif user == 3:
            res = f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Draw" if (user == com) else f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Win" \
                if (user > com + 1) else f"유저 : {rps[user-1]}, 컴퓨터 : {rps[com-1]} 결과 : Lose"
        print(res)
    def quiz04leap(self):
        year = myRandom(2000, 2022)
        res = f'{year}년은 윤년입니다.' if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0) else f'{year}년은 평년입니다.'

        print(res)

    def quiz05grade(self):
        kor = my100()
        eng = my100()
        math = my100()
        sum = self.sum(kor, eng, math)
        avg = self.avg(sum)
        grade = self.grade(avg)
        passChk = self.passChk(grade)
        print(f'국어 : {kor} \n영어 : {eng} \n수학 : {math} \n합계 : {sum} '
              f'\n평균 : {avg} \n등급 : {grade} \n합격여부 : {passChk}')

    def sum(self, kor, eng, math):
        return kor + eng + math

    def avg(self, sum):
        return sum / 3

    def grade(self, avg):
        if avg >= 90:
            res = "A"
        elif avg >= 80:
            res = "B"
        elif avg >= 70:
            res = "C"
        elif avg >= 60:
            res = "D"
        else:
            res = "F"
        return res

    def passChk(self, grade):
        res = '불합격' if grade == 'F' else '합격'
        return res
    @staticmethod
    def quiz06memberChoice():
        members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                   "권혜민", "서성민", "조현국", "김한슬", "김진영",
                   '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                   '최민서', '한성수', '김윤섭', '김승현',
                   "강 민", "최건일", "유재혁", "김아름", "장원종"]
        return members[myRandom(0, 23)]

    def quiz07lotto(self):
        num =myRandom(1,10)
        res = []
        for i in range(0,num):
            li = random.sample(range(1,46), 6)
            li.sort()
            res.append(li)
        print(res)
    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        Account.main()
    def quiz09gugudan(self):  # 책받침구구단
        res = ''
        for i in range(1, 10, 3):
            for j in range(1, 10):
                for k in range(i, (i + 3)):
                    res += f'{k} * {j} = {k * j}\t'
                res += '\n'
            res += '\n'
        print(res)
class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = memberlist()[myRandom(0,23)] if name == None else name
        '''
        self.name = Quiz00.quiz06memberChoice(self)
        num = myRandom(10000000, 99999999)
        self.account_number = f'{str(myRandom(0,99)).rjust(3,"0")} - {(int)(num / 1000000)} - {myRandom(100000,999999)}'
        '''
        self.account_number = self.creat_account_number() if account_number == None else account_number
        self.money = myRandom(100, 999) if money == None else money
    def to_string(self):
        return f'은행 : {self.BANK_NAME} ,\n' \
               f'입금자 : {self.name},\n' \
               f'계좌번호 : {self.account_number},\n' \
               f'금액 : {self.money}\n'
    @staticmethod
    def creat_account_number():
        return "".join([str(myRandom(0, 9)) if i != 3 and i != 6 else '-' for i in range(0, 13)])

    @staticmethod
    def find_account(ls,account_number):
        '''
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                print(ls[i].to_string())
        '''
        return ''.join([j.to_string() if j.account_number == account_number else '찾는 계좌 아님'
                        for i, j in enumerate(ls)])

    @staticmethod
    def del_account(ls, account_number):
        for i , j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def deposit(ls, account_number, money):
        '''
        for i , j in enumerate(ls):
            if j.account_number == account_number:
                j.money += money
                print(ls[i].to_string())
        '''
        return

    @staticmethod
    def wid(ls, account_number, money):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                if (j.money - money) < 0 :
                    print(f'잔액이 부족합니다')
                else:
                    j.money -= money
                    print(ls[i].to_string())
                #print('잔액이 부족합니다') if (j.money - money) < 0 else j.money -=  money
    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌내용 3.입금 4.출금 5.계좌해지 6.계좌조회\n입력 : ')
            if menu == '0':
                break
            elif menu == '1':
                acc = Account(None, None, None)
                print(f'{acc.to_string()} ... 개설 되었습니다.\n')
                ls.append(acc)
            elif menu == '2':
                #for i in range(len(ls)):
                #   print(ls[i])
                a = ''.join(i.to_string() for i in ls)
                print(a)
            elif menu == '3':
                Account.deposit(ls,input('입금할 계좌번호 : '),int(input('입금액 : ')))

            elif menu == '4':

                Account.wid(ls,input('출금할 계좌번호 : '),int(input('출금액 : ')))

            elif menu == '5':
                Account.del_account(ls, input('탈퇴할 계좌번호 : '))

            elif menu == '6':
                print(Account.find_account(ls, input('조회할 계좌번호 : ')))

            else:
                print('Wrong Number.. TryAgain')
