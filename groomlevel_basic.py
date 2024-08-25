
### 정사각형의 개수

N = int(input())

result = N * N

for i in range(2,N+1):
		sqrt = N - i + 1
		result += sqrt * sqrt

print(result)
