# 정수 범위 반복하기 — range

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

`range(stop)` 또는 `range(start, stop, step=1)`은 range 객체를 반환합니다.
정수를 입력받고 stop은 미포함입니다. step=0은 ValueError, 방향과 범위가 맞지 않으면 비어 있습니다.
리스트 전체를 미리 만들지 않으므로 range 자체 저장 공간은 O(1)입니다.

```python
assert list(range(1, 5)) == [1, 2, 3, 4]
assert list(range(4, -1, -1)) == [4, 3, 2, 1, 0]
assert list(range(0, 7, 3)) == [0, 3, 6]
assert list(range(4, 0)) == []
```

`range(arr)`에 리스트를 주면 TypeError입니다. 값만 필요하면 `for x in arr`,
인덱스만 필요하면 `range(len(arr))`를 사용합니다.
