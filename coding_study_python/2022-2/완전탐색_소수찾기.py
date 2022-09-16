import itertools

def isPrime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, num//2+1):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_int = []
    
    for i in range(len(numbers)):
        num = set(itertools.permutations(numbers, i+1))
        for j in num:
            num_int.append(int("".join(j)))
    
    for i in set(num_int):
        if isPrime(i):
            answer += 1
        
    
    return answer




# import itertools

# def isPrime(num):
#     if num == 1 or num == 0:
#         return False
    
#     for i in range(2, num//2 +1):
#         if num % i == 0:
#             return False
    
#     return True
        

# def solution(numbers):
#     answer = 0
#     tmp = []
    
#     for i in range(1,len(numbers)+1):
#         combi = set(itertools.permutations(numbers, i))
#         for j in combi:
#             tmp.append(int("".join(j)))
            
#     for i in set(tmp):
#         if isPrime(i):
#             answer += 1 
#     return answer