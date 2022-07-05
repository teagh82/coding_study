def solution(ans):
    if ans == 1:
        return 1    # 1
    elif ans == 2: 
        return 2    # 1+1, 2
    elif ans == 3:
        return 4    # 1+1+1, 2+1, 1+2, 3
    else:
        return solution(ans-1) + solution(ans-2) + solution(ans-3)
    
T = int(input())

for tc in range(0,T):
    n = int(input())
    print(solution(n))