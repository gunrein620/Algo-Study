# 숫자 문자인지 확인하기 — isdigit

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

문자열은 불변입니다. 이 메서드는 원본을 직접 바꾸지 않으므로 반환값을 사용합니다.

`s.isdigit()`은 비어 있지 않은 문자열의 모든 문자가 digit인지 bool로 반환합니다.
**정수로 바꾸는 함수가 아닙니다.** 부호나 소수점은 digit이 아닙니다.

```python
assert "123".isdigit() is True
assert "a1".isdigit() is False
assert "-12".isdigit() is False
assert "".isdigit() is False
assert "²".isdigit() is True
```

`int("²")`는 ValueError입니다. Unicode의 digit 범위와 int가 받는 문자열 범위가 같지 않습니다.
문제에서 영문과 0~9만 주어진다면 isdigit을 쓰고, ASCII 숫자만 추출하려면 `"0" <= ch <= "9"`를 씁니다.
