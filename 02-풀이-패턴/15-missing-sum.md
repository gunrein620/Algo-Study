# 빠진 값의 합 — 전체에서 있는 것 빼기

[전체 목차](../README.md) · [패턴 목차](README.md) · [문제 복습](../04-복습노트/없는-숫자-더하기.ipynb)

## 이런 문제에서 사용

전체 범위가 정해져 있고, 입력이 중복 없는 부분집합일 때 빠진 원소의 합을 구합니다.
0~9에서 빠진 숫자라면 전체 합은 45입니다.

```python
def solution(numbers):
    return 45 - sum(numbers)

print(solution([1, 2, 3, 4, 6, 7, 8, 0]))  # 14
```

전체 합 45 − 입력 합 31 = 누락된 5 + 9 = 14입니다.
입력에 중복이나 범위 밖 숫자가 있으면 그대로 적용할 수 없습니다.
합이 아니라 빠진 원소 자체가 필요하면 포함 여부를 검사합니다.

```python
numbers = [1, 2, 3, 4, 6, 7, 8, 0]
missing = [num for num in range(10) if num not in numbers]
print(missing)  # [5, 9]
```

입력 길이 m일 때 합을 빼는 풀이의 시간 O(m), 추가 공간 O(1)입니다.

[sum 교과서](../01-파이썬-도구/01-숫자/len-sum-min-max.md)
