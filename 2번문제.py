a = int(input("숫자를 입력하세요: "))

num_list=[]

for i in range(1,a+1):
    if a % i == 0 :
        num_list.append(i)

print(num_list)