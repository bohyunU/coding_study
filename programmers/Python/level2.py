
## 프로그래머스 알고리즘

### 최대값과 최솟값

def solution(s):
    '''
    1. 문자열 읽기
    2. 공백 기준으로 자르기
    3. 리스트에 추가
    4. 리스트에서 min, max return
    '''
    answer = list(map(int, s.split(' ')))
    
    return str(min(answer)) + ' ' + str(max(answer))

## 최솟값 만들기

def solution(A,B):
    '''
    최솟값 * 최대값 순서로 진행
    '''
    
    n = len(A)
    A = sorted(A)
    B = sorted(B, reverse=True)
    result = 0
    
    for i in range(0,n):
        result += A[i] * B[i]
    
    return result

## JadenCase 문자열 만들기

def solution(s):
    
    temp = list(s.split(' '))
    answer = []
    for i in range(0,len(temp)):
        result_temp = ''
        for j in range(0,len(temp[i])):
            if j == 0:
                result_temp += temp[i][j].upper()
            else:
                result_temp += temp[i][j].lower()
        
        answer.append(result_temp)
        
    return " ".join(answer)

## 올바른 괄호

def solution(s):
    '''
    "(" 면 append, ")"이면 pop
    '''
    stack = []
    
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    
    return not stack
    
## 이진 변환 반복하기

def solution(s):
    '''
    1. s가 1이 아닐때까지만 진행.
    2. 횟수를 더하고, 0 개수를 더하고, 길이를 이진법 변환 
    '''
    answer_1 = 0
    answer_2 = 0
    while s != '1':
        answer_1 += 1
        temp = s.count('0')
        answer_2 += temp
        s = s.replace('0','')
        s = str(bin(len(s))[2:])
        
    return answer_1, answer_2
    

