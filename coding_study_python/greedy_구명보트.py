def solution(people, limit):
    answer = 0
    stack = []

    for i in people:
        if not answer:
            answer.append(i)
            continue

        while 1:
            if k <= 0 or not answer:
                break
            if answer[-1] < i:
                answer.pop(-1)
                k -= 1
            else: break
        answer.append(i)

    people.sort()
    sum = 0
    cnt = 0
    for i in people:
        sum += i
        if sum < limit:
            continue
        else: 
            sum = 0
            answer += 1

    answer += len(people) - cnt
    return answer

if __name__ == "__main__":
    print(solution([70, 50, 80, 50], 100), 3)
    print(solution([70, 80, 50], 100), 3)