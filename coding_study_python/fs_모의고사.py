'''
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''

def solution(answers):
    answer = [0,0,0]
    
    n1 = [1, 2, 3, 4, 5] * 2000
    n2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    for i in range(len(answers)):
        if n1[i] == answers[i]:
            answer[0] +=1
        if n2[i] == answers[i]:
            answer[1] +=1
        if n3[i] == answers[i]:
            answer[2] +=1
    
    result = []
    max_correct = max(answer)
    for i in range(len(answer)):
        if answer[i] == max_correct:
            result.append(i+1)
            
        
    return result