# 크기가 작은 부분문자열
# 내 접근은 맞음: p 길이만큼 잘라 숫자로 비교하고 개수를 센다.
# 내 실수: for i in len(t), 자른 값 미저장, 자를 길이를 3으로 고정.


def solution(t, p):
    length = len(p)
    target = int(p)
    answer = 0

    # 마지막 시작 위치 = 전체 길이 - 자를 길이
    # range는 끝을 제외하므로 +1을 붙여 마지막 시작 위치까지 포함.
    for i in range(len(t) - length + 1):
        temp = t[i:i + length]  # 끝 미포함 → 정확히 length글자
        if int(temp) <= target:
            answer += 1

    return answer


# t="3141592", length=3 → 마지막 시작 위치 7-3=4 → range(5)
# i:    0    1    2    3    4
# 조각: 314  141  415  159  592 → 271 이하인 것은 141, 159
# i=5까지 가면 "92"처럼 짧은 조각도 세므로 안 된다.
# int("02")는 2. int로 비교하려던 생각은 맞았다.
print(solution("3141592", "271"))   # 2
print(solution("500220839878", "7"))  # 8
print(solution("10203", "15"))     # 3
print(solution("15", "15"))        # 1: 길이가 같으면 한 번 검사

# 복습: 길이 5에서 2글자씩 자르면 마지막 시작 위치와 range는?
# 답: 마지막 위치 3, range(4). +1을 빼면 마지막 조각을 놓친다.
