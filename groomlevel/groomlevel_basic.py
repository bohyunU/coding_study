
### 정사각형의 개수

N = int(input())

result = N * N

for i in range(2,N+1):
		sqrt = N - i + 1
		result += sqrt * sqrt

print(result)

### 의좋은 형제

first, second = map(int,input().split())
N = int(input())
time = 1

while time <= N:
	if time % 2 != 0:
		if first % 2 != 0:
			give = first // 2 + 1
		else:
			give = first // 2
		
		second += give
		first -= give
		
	else:
		if second % 2 != 0:
			give = second // 2 + 1
		else:
			give = second // 2
		
		first += give
		second -= give
	
	time += 1
				
print(str(first) + ' ' + str(second))