# 약수의 합·개수와 합성수

[전체 목차](../README.md) · [패턴 목차](README.md) · [관련 도구](../01-파이썬-도구/01-숫자/isqrt.md)

“j가 n의 약수”는 `n % j == 0`입니다. n은 양의 정수, j는 1부터 n까지 검사합니다.
합성수는 1보다 크며 소수가 아닌 수, 즉 양의 약수가 3개 이상인 수입니다.

```python
n = 6
assert sum(j for j in range(1, n + 1) if n % j == 0) == 12
assert sum(1 for j in range(1, n + 1) if n % j == 0) == 4
composites = [i for i in range(1, 11)
              if sum(1 for j in range(1, i + 1) if i % j == 0) >= 3]
assert composites == [4, 6, 8, 9, 10]
```

6의 약수는 1,2,3,6이므로 합 12, 개수 4입니다. 1은 소수도 합성수도 아닙니다.
단일 n의 전체 약수 검사는 O(n), 1부터 N까지 위 방식으로 검사하면 O(N²)입니다.
입력이 커지면 약수 쌍을 이용해 제곱근까지만 검사합니다.

```python
from math import isqrt
n = 36
total = 0
for divisor in range(1, isqrt(n) + 1):
    if n % divisor == 0:
        total += divisor
        paired = n // divisor
        if paired != divisor:
            total += paired
assert total == 91
```

6과 6처럼 같은 약수 쌍은 한 번만 더합니다. 반복 횟수는 O(√n), 추가 공간은 O(1)입니다
(일반적인 코테의 정수 연산 비용 가정).
