def solution(r, c):
    answer = [[0 for _ in range(c)] for _ in range(r)] 
    visited = [[0 for _ in range(c)] for _ in range(r)]
    move = [(0, -1),(1, 0),(0, 1),(-1, 0),(0, -1),(-1, 0),(0, 1), (1, 0)]
    
    def dfs(sr, sc, move_idx, cnt):
        if cnt == r * c:
            return
        if move_idx == 3 or move_idx == 7:
            move_idx+=1
        if move_idx == 8:
            move_idx = 0
            
        nr = sr+move[move_idx][0]
        nc = sc+move[move_idx][1]
        cnt+=1
        
        if (nr>=r or nr<0 or nc>=c or nc<0) or visited[nr][nc] == 1:
            move_idx +=1
            if move_idx == 8:
                move_idx = 0
            
            visited[sr+move[move_idx][0]][sc+move[move_idx][1]] = 1
            answer[sr+move[move_idx][0]][sc+move[move_idx][1]] = cnt
            dfs(sr+move[move_idx][0],sc+move[move_idx][1], move_idx, cnt)
        else:
            visited[nr][nc] = 1
            answer[nr][nc] = cnt
            dfs(nr,nc, move_idx, cnt)
    
    answer[0][c-1] = 1
    visited[0][c-1] = 1
    dfs(0,c-1, 0, 1)
    print(answer)
    return answer

if __name__ == '__main__':
    ans = solution(5,4)
    print([[4, 3, 2, 1], [5, 16, 17, 18], [6, 15, 20, 19], [7, 14, 13, 12], [8, 9, 10, 11]]== ans, ans)