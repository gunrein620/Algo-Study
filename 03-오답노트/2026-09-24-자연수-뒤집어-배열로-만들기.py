# 자연수 뒤집어 배열로 만들기
# 내 실수: sorted(..., reverse=True)는 큰 순서 정렬이지 순서 뒤집기가 아니다.
# str(n)도 문자열이므로 바로 [::-1]을 붙일 수 있다.
# 12345 → "12345" → "54321" → [5, 4, 3, 2, 1]


def solution(n):
    return list(map(int, str(n)[::-1]))


print(solution(12345))  # [5, 4, 3, 2, 1]
print(solution(120))    # [0, 2, 1]
