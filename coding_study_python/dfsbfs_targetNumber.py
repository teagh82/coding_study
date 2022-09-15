'''
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
'''

import collections

def solution(numbers, target):
    answer = []
    
    def dfs(sum, idx):
        if idx == len(numbers):
            if sum == target: 
                answer.append(1)
                return len(answer)
        else:
            dfs(sum+numbers[idx], idx+1)
            dfs(sum-numbers[idx], idx+1)
            
    # dfs(0,0)
    # return len(answer)
    
    #### BFS ####
    queue = collections.deque()
    queue.append((numbers[0], 1))
    queue.append((-numbers[0], 1))

    while queue:
        sum, idx = queue.popleft()

        if idx == len(numbers):
            if sum == target:
                answer.append(1)
                # print(1)
        else:
            queue.append((sum + numbers[idx],idx+1))
            queue.append((sum - numbers[idx],idx+1))
        
    return len(answer)