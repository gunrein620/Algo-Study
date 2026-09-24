# 대소문자 바꾸기·확인하기

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

문자열은 불변입니다. 이 메서드는 원본을 직접 바꾸지 않으므로 반환값을 사용합니다.

| 메서드 | 반환 | 의미 |
| --- | --- | --- |
| `s.lower()` | str | 소문자로 변환 |
| `s.upper()` | str | 대문자로 변환 |
| `s.swapcase()` | str | 대문자와 소문자 반전 |
| `s.islower()` | bool | 대소문자 구분 문자가 하나 이상 있고 모두 소문자 |
| `s.isupper()` | bool | 대소문자 구분 문자가 하나 이상 있고 모두 대문자 |

```python
s = "Ab1"
assert s.lower() == "ab1"
assert s.upper() == "AB1"
assert s.swapcase() == "aB1"
assert s == "Ab1"
assert "ABC123".isupper() is True
assert "123".isupper() is False
assert "".islower() is False
assert "".lower() == ""
s = s.lower()
assert s == "ab1"
```

영문 문제에서는 직관적으로 사용하면 됩니다. Unicode에서는 대소문자 변환 시 길이가 변할 수도 있습니다.
