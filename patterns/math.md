# 수학 패턴

[패턴 목차](README.md) · [연산자](../python/syntax/README.md) · [수학 라이브러리](../python/standard-library/README.md)

## 자릿수 — 마지막 자리와 나머지 수

음이 아닌 정수 n에 대해 `n % 10`은 마지막 자리, `n // 10`은 마지막 자리를 제거한 수입니다.
100을 쓰면 두 자리 단위입니다.

```python
assert 1234 % 10 == 4
assert 1234 // 10 == 123
assert 1234 % 100 == 34
assert 1234 // 100 == 12
n = 1234
answer = 0
while n > 0:
    answer += n % 10
    n //= 10
assert answer == 10
assert sum(int(ch) for ch in str(1234)) == 10
assert sum(int(ch) for ch in str(0)) == 0
```

n은 1234 → 123 → 12 → 1 → 0, 합은 4 → 7 → 9 → 10입니다.
while 방식은 n을 바꾸므로 원본이 필요하면 복사합니다. 음수는 먼저 abs를 적용하는 등 조건을 정합니다.
자릿수가 d개일 때 d번 처리합니다. 큰 정수의 연산 비용까지 상수라고 단정하지 않습니다.

### 자릿수를 원래 순서의 반대로 배열에 담기

문제에서 “뒤집어 각 자리 숫자를 배열로”라고 하면 문자열로 바꾸고 순서를 뒤집은 뒤,
각 문자를 정수로 변환합니다. 크기순으로 정렬하는 문제가 아닙니다.

```python
n = 13245
assert list(map(int, str(n)[::-1])) == [5, 4, 2, 3, 1]
assert list(map(int, str(1200)[::-1])) == [0, 0, 2, 1]
```

뒤집힌 문자열 전체를 먼저 int로 바꾸면 앞의 0이 사라지므로 **각 문자에** int를 적용합니다.
문자열로 변환한 뒤 d개 자릿수를 뒤집고 변환하는 단계는 O(d) 시간과 O(d) 공간입니다.
표현식이 낯설면 [함수 반환값에 슬라이싱하기](../python/syntax/README.md#slice-return-value)를 읽고,
[문제 리뷰](../review/2026-09-24-reverse-digits.md)의 질문으로 복습합니다.

## 약수와 합성수

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

## 올림과 최소공배수 — 서로 다른 문제

“남아도 괜찮으니 n명에게 한 조각 이상”은 `(n + pieces - 1) // pieces`입니다.
“남김없이 모두 같은 수의 조각을 받도록”은 n과 pieces의 공배수가 필요합니다.
두 조건을 구분합니다. n과 pieces는 양의 정수입니다.

```python
from math import lcm
n, pieces = 10, 6
assert (n + pieces - 1) // pieces == 2
assert lcm(n, pieces) // pieces == 5
```

두 번째는 30조각을 만들어 10명이 3조각씩 받고, 피자는 5판입니다.

## 분수 덧셈

a/b + c/d의 분자는 a*d+c*b, 분모는 b*d입니다. gcd로 둘을 나누면 약분됩니다.
분모는 양의 정수라고 가정합니다.

```python
from math import gcd
a, b, c, d = 1, 2, 3, 4
numerator = a * d + c * b
denominator = b * d
g = gcd(numerator, denominator)
assert [numerator // g, denominator // g] == [5, 4]
```

분자 10, 분모 8, gcd 2이므로 5/4입니다. 일반 gcd는 작은 수 m에 대해 O(log m)번 정도의
나머지 연산으로 구할 수 있습니다. Fraction으로도 풀 수 있지만 이 원리는 함께 익힙니다.

## 큰 단위부터 사용 — 최적성 확인이 먼저

공격력 5,3,1로 음이 아닌 정수 hp를 정확히 만드는 최소 개수 문제입니다.
이 단위 조합에서는 큰 것부터 채우는 방식으로 최소 개수를 얻을 수 있습니다.

```python
hp = 14
count = hp // 5
hp %= 5
count += hp // 3
hp %= 3
count += hp
assert count == 4  # 5 + 5 + 3 + 1
```

5를 2개 쓰고 4가 남습니다. 3을 1개 쓰고 1이 남아 총 4개입니다.
고정된 세 단위를 계산하므로 일반 정수 연산 비용 가정에서 O(1)입니다.
하지만 **임의의 단위에서 성립하지 않습니다**. 단위가 4,3,1이고 목표가 6이면
큰 것부터는 4+1+1의 3개, 최적은 3+3의 2개입니다.
새 문제에서는 교환 논리나 문제의 단위 구조로 최적성을 확인하고, 안 되면 DP 등을 검토합니다.

## 가져갈 것

- 몫은 사용 횟수, 나머지는 다음에 처리할 양입니다.
- “최소 판 수”와 “남김없이 같은 분배”는 서로 다른 조건입니다.
- 그리디는 큰 것부터 고르는 코드보다 최적성이 성립하는 조건이 먼저입니다.

복습: 36의 약수 합에서 6을 두 번 더하면 안 되는 이유는? → 같은 약수 쌍이기 때문입니다.
