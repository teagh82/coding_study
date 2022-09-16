def solution(n, times):
    times.sort()
    start = 1
    end = times[0]*n    # 총 시간
    
    while start+1 < end:
        cnt = 0                 # mid 시간 안에 담당할 수 있는 인원 수
        mid = (start+end)//2    # 답이 될만한 시간들 
        
        for i in times:         # 답 후보 시간동안 가능한 인원 수
            cnt += mid//i
            
        if cnt >= n:            # end가 답이 될 변수. 인원 수끼리 비교해서 찾아나감
            end = mid
        else:
            start = mid
            
    return end