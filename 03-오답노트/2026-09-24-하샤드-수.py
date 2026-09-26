# 하샤드 수
# 내 실수: while에서 x를 줄여 0으로 만든 뒤 원래 수 대신 0을 검사했다.
# 자릿수는 % 10으로 추출, 누적은 +=. =+는 누적이 아니다.
# "true" 같은 문자열 대신 비교 결과인 True/False를 반환한다.


def solution(x):
    digit_sum = sum(map(int, str(x)))
    return x % digit_sum == 0


# 18 → "18" → 각 문자를 정수 1, 8로 변환 → 합 9 → 18 % 9 == 0
print(solution(18))  # True
print(solution(11))  # False
