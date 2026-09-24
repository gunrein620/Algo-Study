# 인덱스와 값 함께 꺼내기 — enumerate

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

`enumerate(iterable, start=0)`은 `(번호, 값)` tuple을 내놓는 iterator입니다.
start는 번호의 시작값이며 원소를 건너뛰는 인덱스가 아닙니다. 빈 입력이면 아무 쌍도 만들지 않습니다.

```python
arr = ["a", "b"]
assert list(enumerate(arr)) == [(0, "a"), (1, "b")]
assert list(enumerate(arr, start=1)) == [(1, "a"), (2, "b")]
for idx, value in enumerate(arr):
    assert arr[idx] == value
```

관련 개념: [iterable과 iterator — 반복과 소비의 차이](iterable-iterator.md).
