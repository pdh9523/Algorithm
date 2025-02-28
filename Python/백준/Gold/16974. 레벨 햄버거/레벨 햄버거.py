def dnc(N,X):
    if X == 1: return 0

    if X <= burger[N-1]:
        return dnc(N-1, X-1)
    
    if X == burger[N-1]+1:
        return patty[N-1]

    if X == burger[N-1]+2:
        return patty[N-1]+1

    # 이전 버거 패티 + 중간 패티 1장 + 나머지 뒷부분 분할정복 결과
    if X <= burger[N-1] * 2 + 1:
        return patty[N-1] + 1 + dnc(N-1, X - burger[N-1] - 2)
    
    return patty[N]

N,X = map(int,input().split())

burger = [0] * (N+1)
patty = [0] * (N+1)
burger[0] = patty[0] = 1

for i in range(1,N+1):
    # 버거 하나의 전체 크기
    burger[i] = burger[i-1] * 2 + 3
    # 버거 하나의 패티 개수
    patty[i] = patty[i-1] * 2 + 1

print(dnc(N,X))