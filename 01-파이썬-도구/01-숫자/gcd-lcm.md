# 최대공약수·최소공배수 — gcd와 lcm

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

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
