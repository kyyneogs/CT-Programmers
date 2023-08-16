def solution(k, m, score):
    score.sort(reverse=True)
    sum = 0
    for i, j in enumerate(score, start=1):
        if i%m==0: sum=sum+j*m
    return sum

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))