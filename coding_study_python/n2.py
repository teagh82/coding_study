def solution(names, homes, grades):
    rank = [_ for _ in range(len(names))]
    rank.sort(key = lambda x: (-int(grades[x]//1), -(homes[x][0] ** 2 + homes[x][1] ** 2), names[x]))
    # for i in range(len(names)):
    #     rank[i] += 1
              
              
        
#     rank = [[0 for _ in range(3)] for a in range(len(names))]
#     for i in range(len(names)):
#         rank[i][0] = -int(grades[i]//1)
#         rank[i][1] = -(homes[i][0]*homes[i][0] + homes[i][1]*homes[i][1])
#         rank[i][2] = names[i]
    
#     rank.sort()
    
    # rank2 = list(map(list, zip(*rank)))[2]
    answer = [rank.index(a)+1 for a in names]
    return answer 