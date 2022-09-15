'''
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
'''

import itertools

def isPrime(num):
    if num == 1 or num == 0:
        return False
    
    for i in range(2, num//2 +1):
        if num % i == 0:
            return False
    
    return True
        

def solution(numbers):
    answer = 0
    tmp = []
    
    for i in range(1,len(numbers)+1):
        combi = set(itertools.permutations(numbers, i))
        for j in combi:
            tmp.append(int("".join(j)))
            
    for i in set(tmp):
        if isPrime(i):
            answer += 1 
    return answer