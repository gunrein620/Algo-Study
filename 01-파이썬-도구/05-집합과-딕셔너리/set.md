# 중복 제거와 집합 연산 — set

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

`set(iterable)`은 중복 없는 set을 반환합니다. 원본을 변경하지 않으며 순서를 보장하지 않습니다.
원소는 hashable이어야 하므로 리스트를 원소로 넣으면 TypeError입니다.
빈 집합은 `set()`이며 `{}`는 빈 dict입니다.

```python
a = set([1, 1, 2])
b = {2, 3}
assert a == {1, 2}
assert a & b == {2}
assert a | b == {1, 2, 3}
assert a - b == {1}
a.add(4)
assert 4 in a
```

`add`는 원본을 변경하고 None을 반환합니다. 집합 포함 검사는 평균 O(1)이며,
리스트 포함 검사는 최악 O(n)입니다. 집합 순서를 정렬 순서로 착각하지 않습니다.
