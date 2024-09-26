
### Python 51 ~ 100


## 완전제곱수

import sys
import math

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

start = math.ceil(M**(1/2))
end = math.floor(N**(1/2))

result = []

for i in range(start, end+1):
    check = i**2
    if check >= M and check <= N:
        result.append(check)
        
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
    

## 첼시를 도와줘

N = int(input())

# 각 테스트 케이스마다 처리
for i in range(N):
    # 고려해야할 선수의 수 입력
    M = int(input())
    player_dict = {}
    
    # 선수 정보 입력
    for j in range(M):
        sal, name = input().split()
        player_dict[int(sal)] = name
    
    # 가장 비싼 선수의 이름 출력
    print(player_dict[max(player_dict)])
    
    
    
## 생일

N = int(input())

people_list = {}
for i in range(N):
    name, day, mon, year = input().split()
    if len(mon) == 1:
        mon = '0' + mon
    if len(day) == 1:
        day = '0' + day
    birth = int(year + mon + day)
    people_list[birth] = name

print(people_list[max(people_list)])
print(people_list[min(people_list)])
    