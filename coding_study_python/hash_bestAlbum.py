import collections

def solution(genres, plays):
    answer = []
    
    music_dic = dict(zip(genres, [0 for _ in range(len(genres))]))
    music_zip = list(zip(genres, plays))
    print(music_dic)
    print(music_zip)
    
    for i in music_zip:
        for j in set(genres):
            if i[0] == j:
                music_dic[j] += i[1]
    
    album = [[0 for _ in range(4)] for a in range(len(genres))]
    for i in range(len(genres)):
        album[i][0] = music_dic[genres[i]]
        album[i][1] = plays[i]
        album[i][2] = -i
        album[i][3] = genres[i]

    album.sort(reverse = True)
    
    tmp = 0
    tmp_gen = ""
    for i in range(len(album)):
        if tmp == 2 and tmp_gen == album[i][3]:
            continue
        if tmp_gen != album[i][3]:
            tmp = 0
        tmp_gen = album[i][3]
        answer.append(album[i][2] * (-1))
        tmp += 1
    
    return answer