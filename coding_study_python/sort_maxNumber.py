'''
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
'''

import functools

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(lambda x,y: int(x+y)-int(y+x)), reverse=True)    
        
    return str(int("".join(numbers)))