'''
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
'''

def dfs(graph, start, visited):
    if visited[start]:
        return 0
    else: 
        visited[start] = True
        for node in range(len(graph)):
            if graph[start][node] == 1:
                dfs(graph, node, visited)
        return 1
    return 0

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        answer += dfs(computers, i, visited)

    return answer