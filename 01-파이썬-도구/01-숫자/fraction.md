# 정확한 분수 계산 — Fraction

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

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
직접 분수를 구현하는 원리는 [수학 패턴](../../02-풀이-패턴/13-fraction-add.md)에 있습니다.
