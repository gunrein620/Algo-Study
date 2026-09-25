# 나누어 떨어지는 숫자 배열
# 내 실수: [i for i in arr if 조건 else -1]은 문법 오류.
# 뒤쪽 if는 걸러내기: [i for i in arr if 조건]
# 앞쪽 if/else는 값 바꾸기: [i if 조건 else -1 for i in arr]
# 이 문제는 원소마다 -1을 넣는 게 아니라 결과 전체가 비었을 때 [-1].


def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    return answer or [-1]


# a or b: a가 거짓으로 평가되면 b, 아니면 a를 반환한다.
# []는 거짓, [0]은 비어 있지 않아서 참.
print(solution([5, 9, 7, 10], 5))  # [5, 10]
print(solution([3, 2, 6], 10))     # [-1]
