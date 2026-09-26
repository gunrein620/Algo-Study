# 정수 내림차순으로 배치하기
# 내 실수: map(int, ...)로 정수들을 만든 뒤 join에 넣었다.
# join은 문자열끼리 합친다. 모두 합친 뒤 마지막에 int로 바꾼다.
# sorted는 리스트 반환, join은 문자열 반환, int는 정수 반환.


def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))


print(solution(118372))  # 873211
