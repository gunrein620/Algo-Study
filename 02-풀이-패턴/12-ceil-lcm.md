# 최소 묶음 수와 남김없는 분배

[전체 목차](../README.md) · [패턴 목차](README.md) · [관련 도구](../01-파이썬-도구/01-숫자/gcd-lcm.md)

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
