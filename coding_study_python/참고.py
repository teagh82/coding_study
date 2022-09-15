# int 리스트 값을 str로 바꾸기
numbers = list(map(str, numbers))

# 정렬 조건 바꾸기 (x+y)>(y+x)가 되도록 reverse 내립차순 정렬
numbers.sort(key=functools.cmp_to_key(lambda x,y: int(x+y)-int(y+x)), reverse=True)

# 리스트 값들 합치기    
str(int("".join(numbers)))

# str p2가 str p1으로 시작하는지 t/f로 나타냄
p2.startswith(p1)

# 조합을 구할 때는 곱하기

# kind 배열에 있는 요소들의 등장 개수를 카운터 객체로 나타냄
# [('headgear', 2), ('eyewear', 1)]
cnt = collections.Counter(kind).most_common()

# genres의 요소들:0 으로 딕셔너리 생성
# 	{'classic': 0, 'pop': 0}
music_dic = dict(zip(genres, [0 for _ in range(len(genres))]))

# genres:plays로 리스트 생성
# [('classic', 500), ('pop', 600), ('classic', 150), ('classic', 800), ('pop', 2500)]
music_zip = list(zip(genres, plays))

# list에서 조건에 맞게 요소 뽑기
# citations의 요소 중 h보다 크거나 같은 것만 뽑아서 리스트 만들고 개수를 셈
cnt_h = len(list(filter(lambda x:x>=h, citations)))
cnt_l = len(list(filter(lambda x:x<=h, citations)))

# 소수찾기
def isPrime(num):
    if num == 1 or num == 0:
        return False
    
    for i in range(2, num//2 +1):
        if num % i == 0:
            return False
    
    return True

# 모든 조합을 찾음 
# numbers 배열에서 i개의 숫자를 골라 만든 조합
import itertools
combi = set(itertools.permutations(numbers, i))

# dfs - Q: target number
def dfs(sum, idx):
    if idx == len(numbers):
        if sum == target: 
            answer.append(1)
            return len(answer)
    else:
        dfs(sum+numbers[idx], idx+1)
        dfs(sum-numbers[idx], idx+1)
# dfs - Q: network 
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

# bfs - Q: target number
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