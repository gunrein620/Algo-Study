# 두 값 교환하기 — swap

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

Python은 `a, b = b, a`로 교환합니다. 오른쪽 값을 먼저 평가하고 왼쪽에 대입합니다.
문자열의 개별 위치는 수정할 수 없으므로 리스트로 변환하고 마지막에 join합니다.

```python
arr = list("abc")
arr[0], arr[2] = arr[2], arr[0]
assert "".join(arr) == "cba"
```
