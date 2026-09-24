# 문자·숫자·리스트로 타입 바꾸기

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

| 내장 타입 생성자 | 입력 → 반환 | 주의 |
| --- | --- | --- |
| `int(x)` | 정수 문자열/수 → int | 잘못된 문자열은 ValueError; 실수는 0 방향으로 절삭 |
| `str(x)` | 객체 → str | 숫자도 문자로 변환 |
| `list(iterable)` | iterable → list | 원소는 얕게 복사; 인자 없으면 [] |
| `tuple(iterable)` | iterable → tuple | 변경 불가능한 순서열; 인자 없으면 () |

```python
assert int("-123") == -123
assert str(123) == "123"
assert "1" != 1
assert list("abc") == ["a", "b", "c"]
assert tuple([1, 2]) == (1, 2)
assert int(-3.9) == -3
```
