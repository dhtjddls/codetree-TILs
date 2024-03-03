def process_input(input_str):
    result = []
    cursor_position = 0

    for char in input_str:
        if char.isalpha() or char.isdigit():
            # 알파벳 소문자, 대문자, 숫자인 경우 현재 커서 위치에 문자 추가
            result.insert(cursor_position, char)
            cursor_position += 1
        elif char == '-':
            # 명령어 '-'인 경우 바로 앞의 문자 하나 제거
            if cursor_position > 0:
                result.pop(cursor_position - 1)
                cursor_position -= 1
        elif char == '<':
            # 명령어 '<'인 경우 왼쪽으로 한 칸 커서 이동
            cursor_position = max(0, cursor_position - 1)
        elif char == '>':
            # 명령어 '>'인 경우 오른쪽으로 한 칸 커서 이동
            cursor_position = min(len(result), cursor_position + 1)

    return ''.join(result)

# 입력 받기
input_str = input().strip()

# 결과 출력
output_str = process_input(input_str)
print(output_str)