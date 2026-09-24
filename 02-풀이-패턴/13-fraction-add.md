# 분수 덧셈과 약분

[전체 목차](../README.md) · [패턴 목차](README.md) · [관련 도구](../01-파이썬-도구/01-숫자/fraction.md)

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
