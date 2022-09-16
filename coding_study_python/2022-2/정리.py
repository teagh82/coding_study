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

### 정렬은 시간초과때문에 단순하게 풀면 안됨 고려해야함
### 그럴 때 sort(key)로 커스텀해서 정렬하면 속도 빠름
numbers_str.sort(key = functools.cmp_to_key(lambda x,y: int(x+y) - int(y+x)), reverse = True)
# cmp_to_key()안의 값이 0보다 크도록 정렬
# 위의 예제는 x+y가 더 크면 그대로 x,y 순서
# y+x가 더 크면 y,x 순서

### 리스트 요소의 타입 변경하기
list(map(str, list_name))
list(map(int, list_name))

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


### 수학
import math
math.ceil(3.22) # 올림
math.floor(3.2) # 내림
math.trunc(3.22) # 반올림

### 배열의 요소 개수 세서 딕셔너리로 만들기
import collections
l = [1,1,2,2,3]
dict(collections.Counter(l))


### 덱
# 덱을 사용하면 효율이 좋음
from collections import deque
d = deque([1,2,3])
d.popleft()
d.append
deque.append(item)# item을 데크의 오른쪽 끝에 삽입한다.
deque.appendleft(item)# item을 데크의 왼쪽 끝에 삽입한다.
deque.pop()# 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.popleft()# 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.extend(array)# 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
deque.extendleft(array)# 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
deque.remove(item)# item을 데크에서 찾아 삭제한다.
deque.rotate(num)# 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).