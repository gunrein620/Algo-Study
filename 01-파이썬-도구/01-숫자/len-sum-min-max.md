# 길이·합계·최솟값·최댓값

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

| 내장함수 | 입력과 문법 | 반환값 | 빈 입력 |
| --- | --- | --- | --- |
| `len(obj)` | 길이가 있는 문자열·리스트·딕셔너리 등 | 원소 수 `int` | `0` |
| `sum(iterable, start=0)` | 더할 수 있는 수들 | 합; 타입은 원소와 start에 따름 | start, 기본 `0` |
| `min(iterable)` | 서로 비교할 수 있는 원소들 | 가장 작은 원소 | `ValueError` |
| `max(iterable)` | 서로 비교할 수 있는 원소들 | 가장 큰 원소 | `ValueError` |

원본을 바꾸지 않습니다. min/max는 `min(a, b)`처럼 여러 인자도 받습니다.
iterable 한 개를 넣는 형식에서는 `default=`로 빈 입력의 결과를 정할 수 있습니다.
`len`은 모든 iterable에 되는 것이 아닙니다. map이나 제너레이터는 직접 길이를 물을 수 없습니다.

```python
arr = [3, 1, 2]
assert len(arr) == 3
assert sum(arr) == 6
assert sum([]) == 0
assert min(arr) == 1
assert max(arr) == 3
assert max([], default=0) == 0
assert sum(arr) / len(arr) == 2.0
```

평균은 빈 리스트에서 0으로 나누므로 별도 조건이 필요합니다. `sum`은 문자열 연결용이 아닙니다.
길이 n인 일반 리스트 기준 len은 O(1), 합·최솟값·최댓값은 O(n)입니다.
