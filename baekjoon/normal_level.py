
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
    