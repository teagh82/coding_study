### 이차원 배열 컴프리헨션
albums = [[0 for i in range(4)] for _ in genres]
'''
albums[장르수][0]
albums[장르수][1]
albums[장르수][2]
albums[장르수][3]
'''

### 정렬은 key 사용해서 정렬 순서 정할 수 있음
for idx, i in enumerate(genres):
    albums[idx][0] = play_sum[i]    # 장르별 재생 합
    albums[idx][1] = plays[idx]     # 재생 수
    albums[idx][2] = idx            # 고유번호
    albums[idx][3] = genres[idx]    # 장르
        
albums.sort(key = lambda x:(x[0], x[1], -x[2]), reverse = True)

### sorted도 가능
sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)

### zip을 쓰면 두개의 리스트를 합칠 수 있음 
### 기본은 튜플로 합쳐짐
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for i in range(3):
     pair = (numbers[i], letters[i])
     print(pair)
     
# 결과    
(1, 'A')
(2, 'B')
(3, 'C')

# 언패킹도 가능
numbers, letters = zip(*pairs)
# 결과
numbers
(1, 2, 3)
letters
('A', 'B', 'C')

# 딕셔너리 합치기도 가능
keys = [1, 2, 3]
values = ["A", "B", "C"]
dict(zip(keys, values))
{1: 'A', 2: 'B', 3: 'C'}

# 병렬처리도 가능
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
     print(number, upper, lower)
# 결과
'''
1 A a
2 B b
3 C c
4 D d
5 E e
'''

# 행렬 바꿀 때는 zip(*list_name) 사용
list(zip( *arr ))
# 가끔 for문을 돌면서 가로의 합, 세로의 합을 구해야될 때 가 있음!
# 가로의 합은 평소대로 이중 for문 돌면서 구할 수 있지만, 세로의 합은 구하기가 좀 번거로움!
# 그럴 때 행과 열을 바꿔주면, 평소대로 이중 for문 돌면서 세로의 합도 구할 수 있다!
[1 2 3]               [1 4 7]
[4 5 6]      ->       [2 5 8]
[7 8 9]               [3 6 9]
# *arr                 zip(*arr)


# 90도 회전
list(zip( *arr[::-1] ))
[1 2 3]              [7 8 9]              [7 4 1]
[4 5 6]      ->      [4 5 6]      ->      [8 5 2]
[7 8 9]              [1 2 3]              [9 6 3]
# *arr               *arr[::-1]         zip(*arr[::-1])