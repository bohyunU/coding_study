
### A + B

first,second = map(int,input().split())

print(first + second)

### A / B

up, down = map(int,input().split())

print(up / down)


### 오븐 시계

hour, min = map(int, input().split())
min_plus = int(input())

hour += (min + min_plus) // 60
min = (min + min_plus) % 60

hour = hour % 24

print(hour, min)


### 팰린드롬인지 확인하기

word = input()

temp = list(word)
first = ''
second = ''
if len(word) % 2 == 0:    
    for i in range(0,len(temp)//2):
        first = first + temp[i]

    for i in range(len(temp)-1,len(temp)//2-1, -1):
        second = second + temp[i]
else:
    for i in range(0,len(temp)//2):
        first = first + temp[i]

    for i in range(len(temp)-1,len(temp)//2, -1):
        second = second + temp[i]

if first == second:
    print(1)
else:
    print(0)
