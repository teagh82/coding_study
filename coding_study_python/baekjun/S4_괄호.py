T = int(input())

for tc in range(T):
    stack = []
    str = input()
    for i in str:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else: # 스택이 비어있다면 (가 부족한 것. 괄호X
                print("NO")
                break
    else: 
        if not stack: # 스택이 비어있다면 괄호O
            print("YES")
        else: # 끝까지 갔는데 스택에 괄호가 남아있다면 )가 부족한 것. 괄호X
            print("NO")
            
            

T = int(input())

for tc in range(0,T):
    str = input()
    l = 0
    r = 0
    tl = 0
    tr = 0
    check = 0
    for i in str:
        if i == "(":
            l += 1
        elif i == ")":
            r += 1
        tl = l
        tr = r
        if tl < tr:
            print("NO")
            check = 1
            break
        
        if l == r:
            tl= l-r if (l-r)>0 else 0
            tr= r-l if (r-l)>0 else 0
            l = tl
            r = tr
            
    if check == 0:
        if l != r:
            print("NO")
        else:
            print("YES")
        
