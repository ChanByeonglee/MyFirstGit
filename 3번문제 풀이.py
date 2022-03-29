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

    #먼저 정렬하기.
    num_list.sort()

    my_num_list = []  # 중복없이 정렬된 리스트를 만들 예정
    my_max_list = []  # 최고 중복을 가진 수를 추가할 예정
    my_max_num = 0  # 최고 중복이 몇개인지 기록할 예정
    current_num = 1  # 현재 요소가 중복이 몇개인지 기록할 예정

    my_num_list.append(num_list[0])
    for i in range(99):
        if num_list[i] != num_list[i+1] :
            my_num_list.append(num_list[i+1])
            if current_num == my_max_num :
                my_max_list.append(num_list[i])
            elif current_num > my_max_num :
                my_max_num = current_num
                my_max_list = [num_list[i]]
            current_num = 1
        elif num_list[i] == num_list[i+1] :
            current_num += 1


    #문제 1번

    print("최고 중복 수는",my_max_num,"이들의 모임은",my_max_list)

    #문제 2번

    print("3번째로 큰 수는", my_num_list[-3])

    #문제 3번
    print(my_num_list)

    # 이제 3문제는 my_num_list와 my_max_list, my_max_num을 이용해서 아래에 직접 풀기.
    # ----------------------------------------------------------------------------------------------#












