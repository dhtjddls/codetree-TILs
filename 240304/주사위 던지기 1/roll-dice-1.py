from itertools import product

# 입력 받기
N, M = map(int, input().split())

# 주사위 눈의 범위
dice_faces = range(1, 7)

# 경우의 수 생성
all_outcomes = list(product(dice_faces, repeat=N))

if M == 1:
    # 모든 경우의 수 출력
    for outcome in all_outcomes:
        print(*outcome)
elif M == 2:
    # 중복된 경우 배제하고 출력
    unique_outcomes = set(all_outcomes)
    for outcome in unique_outcomes:
        print(*outcome)
elif M == 3:
    # 중복된 눈이 나오지 않는 경우만 출력
    unique_no_duplicate_outcomes = set(outcome for outcome in all_outcomes if len(set(outcome)) == N)
    for outcome in unique_no_duplicate_outcomes:
        print(*outcome)