
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