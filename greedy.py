#n,m,k 공백으로 구분하여 입력받기
n,m,k=map(int,input().split())
#n개의 수를 고백으로 구분하여 입력받기
data=list(map(int,input().split()))

#입력받은 수들 정렬하기
data.sort()
first=data[n-1] 
second=data[n-2]

result=0

while True:
    for i in range (k):
        if m==0:
            break
        result += first
        m -= 1
    if m==0:
        break
    result += second
    m -= 1
print(result)