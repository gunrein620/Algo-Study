# 03. 표준 라이브러리

[전체 목차](../../README.md) · [빈도 패턴](../../patterns/counting-mapping.md) · [수학 패턴](../../patterns/math.md)

여기 있는 도구는 내장함수와 달리 import가 필요합니다. 외부 패키지를 설치할 필요는 없습니다.

## collections.Counter — 전체 빈도를 한 번에

`Counter(iterable)`은 원소 → 개수의 Counter 객체(dict의 하위 클래스)를 만듭니다.
원본은 변경하지 않으며 원소는 hashable이어야 합니다. 빈 입력은 빈 Counter,
없는 key 조회는 0입니다. 이건 코테에서 자주 쓰니 챙깁니다.

```python
from collections import Counter
cnt = Counter([1, 1, 2, 3, 3, 3])
assert cnt[3] == 3
assert cnt[9] == 0
assert list(cnt.values()) == [2, 1, 3]
assert list(cnt.items()) == [(1, 2), (2, 1), (3, 3)]
assert cnt.most_common(1) == [(3, 3)]
assert Counter().most_common(1) == []
```

`most_common(k)`는 `(값, 빈도)` tuple들의 list를 반환합니다.
동률은 먼저 나타난 순서입니다. “최빈값 동률이면 -1” 같은 문제 조건을 자동으로 해결하지 않습니다.
길이 n의 입력을 세는 것은 평균 O(n), 서로 다른 값이 u개면 저장 공간 O(u)입니다.

## math.gcd / lcm — 최대공약수와 최소공배수

정수 a, b를 받아 음수가 아닌 int를 반환합니다. gcd는 공통 약수 중 최대,
lcm은 공통 배수 중 최소 양수입니다(인수에 0이 있으면 lcm은 0).

```python
from math import gcd, lcm
assert gcd(12, 18) == 6
assert lcm(12, 18) == 36
assert gcd(0, 0) == 0
assert lcm(0, 5) == 0
numerator, denominator = 10, 8
g = gcd(numerator, denominator)
assert [numerator // g, denominator // g] == [5, 4]
```

분수의 분모는 0이 아니어야 합니다. lcm은 Python 3.9 이상에서 제공합니다.

## math.isqrt — 정수 제곱근

`isqrt(n)`은 0 이상의 정수 n에 대해 제곱근을 내린 정확한 int를 반환합니다.
음수면 ValueError, 실수면 TypeError입니다. 부동소수점 sqrt의 반올림 오차를 피할 수 있습니다.

```python
from math import isqrt
assert isqrt(15) == 3
assert isqrt(16) == 4
assert isqrt(0) == 0
n = 16
r = isqrt(n)
assert r * r == n
```

## fractions.Fraction — 정확한 분수 계산

`Fraction(분자, 분모)`는 약분된 Fraction 객체입니다. 분모가 0이면 ZeroDivisionError입니다.
`numerator`, `denominator` 속성은 int이며, 분모의 부호는 양수로 정리됩니다.

```python
from fractions import Fraction
answer = Fraction(1, 2) + Fraction(3, 4)
assert answer.numerator == 5
assert answer.denominator == 4
assert Fraction(0, 7) == 0
assert Fraction("0.1") == Fraction(1, 10)
```

`Fraction(0.1)`은 부동소수점 0.1의 실제 저장값을 분수로 바꿉니다.
정확한 십진수 의도는 문자열이나 정수 분자/분모로 전달합니다.
직접 분수를 구현하는 원리는 [수학 패턴](../../patterns/math.md)에 있습니다.

## 다음에 배울 도구 — 학습 예정

아래는 탐색용 지도이며 숙달 완료 목록이 아닙니다. 실제로 배울 때 예제·예외·풀이를 추가합니다.

| 도구 | 가져오기 | 먼저 알아둘 용도·주의 |
| --- | --- | --- |
| deque | `from collections import deque` | 큐/BFS, popleft로 앞에서 제거; 빈 큐 제거는 IndexError |
| defaultdict | `from collections import defaultdict` | 그룹핑, 없는 key 조회 시 기본값 생성 |
| heapq | `import heapq` | 최소 힙, heappush/heappop; 빈 힙 pop은 IndexError |
| bisect | `import bisect` | 정렬된 배열의 삽입 위치; bisect_left는 왼쪽 경계 |
| combinations | `from itertools import combinations` | 순서 없는 r개 선택; iterator 반환 |
| permutations | `from itertools import permutations` | 순서 있는 r개 나열; iterator 반환 |

## 복습

1. Counter에 없는 key를 조회하면? → 0.
2. 15의 isqrt는? → 3. 제곱수 확인은 `r*r == n`.
3. Fraction의 분자·분모를 얻는 방법은? → numerator, denominator 속성.
