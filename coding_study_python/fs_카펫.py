'''
Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''

def solution(brown, yellow):
    answer = []
    total = brown+yellow

    for i in range(1,total):
        w = i
        h = total // i
        
        if w >= h and total == w*h:
            if (w-2) * (h-2) == yellow:
                answer = [w,h]
                break
    
    return answer