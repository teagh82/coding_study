'''
예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1 
1
1
0
0
1
'''

ac = int(input())
A = list(map(int, input().split()))
bc = int(input())
B = list(map(int, input().split()))
A.sort()

# 이진탐색 이용
def bs(start, end, target):
    while start <= end:
        #중간을 기준으로 target 검색
        mid = (start+end)//2
        if A[mid] == target: 
            return 1
        #찾으려는 값이 오른쪽에 존재
        if A[mid] < target:
            start = mid + 1
        #찾으려는 값이 왼쪽에 존재 
        elif A[mid] > target:
            end = mid - 1
    #못찾는 경우
    return 0

for i in B:
    print(bs(0,ac-1,i))


'''
이진탐색

#찾는데 기준이 되는 배열이 a라고 했을시,
def bs(start, end, target):
    while start <= end:
        #반을 기준으로 찾으려는 값(target)을 검색
        mid = (start+end)//2
        if a[mid] == target: return 1
        #찾으려는 값이 기준 보다 큼, 즉 반절로 나눴을 때 오른쪽에 존재
        if a[mid] < target:
            start = mid + 1
        #찾으려는 값이 기준 보다 작음, 즉 반절로 나눴을 때 왼쪽에 존재 
        elif a[mid] > target:
            end = mid - 1
    #못찾음
    return 0
'''