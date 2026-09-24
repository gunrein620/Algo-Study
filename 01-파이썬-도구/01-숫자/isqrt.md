# isqrt — 정수 제곱근 구하기·제곱수 판별하기

[전체 목차](../../README.md) · [도구 목차](../README.md) · [숫자 계산 목차](README.md)

**`isqrt(n)`은 제곱근을 내림한 정수를 반환합니다. 제곱수 판별은 그 결과를 다시 제곱해서 확인합니다.**

## 바로 쓰는 코드

```python
from math import isqrt

n = 16
r = isqrt(n)
is_square = r * r == n
assert is_square is True
```

## 입력과 반환값

| 항목 | 내용 |
| --- | --- |
| 가져오기 | `from math import isqrt` — math 모듈에서 제공 |
| 문법 | `isqrt(n)` |
| 입력 | 0 이상의 정수 n |
| 반환 | 제곱근을 내림한 `int`; True/False가 아님 |
| 원본 변경 | 없음 |
| 0 입력 | 0 반환 |
| 잘못된 입력 | 음수는 ValueError, 실수는 TypeError |

## 실제 값으로 이해하기

| n | 제곱근 | `r = isqrt(n)` | `r * r == n` |
| --- | --- | --- | --- |
| 15 | 약 3.87 | 3 | `9 == 15` → False |
| 16 | 4 | 4 | `16 == 16` → True |
| 25 | 5 | 5 | `25 == 25` → True |
| 0 | 0 | 0 | `0 == 0` → True |

```python
from math import isqrt
assert isqrt(15) == 3
assert isqrt(16) == 4
assert isqrt(0) == 0
n = 16
r = isqrt(n)
assert r * r == n
```

## 왜 다시 제곱하는가?

15처럼 제곱수가 아닌 수도 isqrt의 결과는 정수입니다. 따라서 `isqrt(n)`이 정수인지 확인해서는 판별할 수 없습니다.
반환된 r을 제곱했을 때 원래 n과 정확히 같아야 제곱수입니다.

부동소수점 sqrt의 반올림 오차를 피하고 정확하게 정수 제곱근을 구할 수 있습니다.
입력 조건이 0 이상인지 확인한 뒤 사용합니다.

## 함께 읽기

- [약수 쌍을 제곱근까지만 검사하기](../../02-풀이-패턴/11-divisors.md)
- [나눗셈·몫·나머지](division.md)

## 복습 질문

`isqrt(24)`가 4일 때, 24가 제곱수가 아닌 이유는?

<details>
<summary>답 확인</summary>

4 × 4는 16이고 24와 다르기 때문입니다. isqrt가 정수를 반환한다는 사실만으로는 제곱수라고 할 수 없습니다.

</details>
