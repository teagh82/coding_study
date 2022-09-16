from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])   # 갈 수 대수 만큼 넣음
    complete = deque()
    truck_len = len(truck_weights)
    
    while len(complete) != truck_len:
        answer += 1
        tmp = bridge.popleft()
        
        # 다리 마지막에 트럭 있다면 완료에 추가
        if tmp != 0:
            complete.append(tmp)
            
        # 다리가 비어있지 않을 때 무게, 길이가 이하라면 새로운 트럭 다리에 추가
        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())        
        else:
            bridge.append(0)    # 못들어갔으니까 0
            
    
    return answer









'''
def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = list(0 for _ in range(bridge_length))
    complete = []
    truck_len = len(truck_weights)

    while len(complete) < truck_len:
        answer += 1
        tmp = bridge.pop(0)
        if tmp != 0:
            complete.append(tmp)
        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

    return answer
'''