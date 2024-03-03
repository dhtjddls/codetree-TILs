def min_boxes(n):
    # 5의 용량을 가진 상자와 3의 용량을 가진 상자에 나누어 담는데 필요한 상자의 최소 개수 계산
    # 가능한 한 많은 5의 용량 상자를 사용하고, 나머지를 3의 용량 상자로 채움
    
    # 5의 용량 상자 개수
    box_5 = n // 5
    
    # 남은 양이 5의 용량으로 나누어 떨어진다면
    if n % 5 == 0:
        return box_5
    else:
        # 5의 용량으로 나누어 떨어지지 않으면 3의 용량 상자를 추가로 사용해야 함
        while box_5 >= 0:
            # 가능한 한 많은 5의 용량 상자를 사용하고 나머지를 3의 용량 상자로 채움
            remaining_capacity = n - box_5 * 5
            if remaining_capacity % 3 == 0:
                return box_5 + (remaining_capacity // 3)
            else:
                box_5 -= 1
    
    # 정확하게 나눌 수 없는 경우
    return -1

# 입력 받기
n = int(input())

# 결과 출력
result = min_boxes(n)
print(result)