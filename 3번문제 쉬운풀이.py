import random

"""
돌쇠 2주차 상급문제.

1. 숫자 리스트는 num_list에 저장되어있다.
2. 숫자의 갯수는 100개이고, 숫자의 범위는 0~99이다.
3. 방법은 자유로우나, 깔끔할수록 고득점. 

"""

def create():
    temp = [random.randint(0, 99) for i in range(100)]

    return temp


if __name__ == "__main__":

    num_list = create()
    ##### Do not modify above #####
    #####여기 밑에다가 코딩하세요######

    my_new_list = [0]*100  #0으로 가득찬 100개짜리 리스트 생성, 인덱스 범위는 0~99이다.

    for i in range(100):
        my_new_list[num_list[i]] += 1 #ex) my_new_list의 30번 인덱스는 num_list 안에 30이 몇개인지 기록되어있다.

    #1번#

    max = 0 #최대 중복 횟수
    my_max_list=[] #최대 중복 수 모임

    #최대 중복 횟수를 찾기
    for i in range(100) :
        if max < my_new_list[i] :
            max = my_new_list[i]

    #최대 중복 수 모임 만들기
    for i in range(100) :
        if max == my_new_list[i] :
            my_max_list.append(i)


    #2번,3번#

    my_answer_list=[]

    #한번이라도 나온 수는 추가하기
    for i in range(100):
        if my_new_list[i] != 0 :
            my_answer_list.append(i)

    print("최대 중복 수는 ",max,"해당하는 숫자들은 ",my_max_list)
    print("3번째로 큰 수는 ",my_answer_list[-3])
    print(my_answer_list)







