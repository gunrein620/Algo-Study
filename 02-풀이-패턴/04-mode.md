# 최빈값 구하기 — 동률 처리

[전체 목차](../README.md) · [패턴 목차](README.md) · [관련 도구](../01-파이썬-도구/05-집합과-딕셔너리/counter.md)

“가장 많이 나온 값, 동률이면 -1”이라는 조건을 가정합니다. Counter로 한 번에 세고 최대 빈도를 찾습니다.

```python
from collections import Counter

def mode_or_minus_one(arr):
    if not arr:
        return -1  # 이 예제에서 정한 빈 입력 규칙
    counts = Counter(arr)
    highest = max(counts.values())
    winners = [value for value, count in counts.items() if count == highest]
    return winners[0] if len(winners) == 1 else -1

assert mode_or_minus_one([1, 1, 2, 3, 3, 3]) == 3
assert mode_or_minus_one([1, 1, 2, 2]) == -1
assert mode_or_minus_one([]) == -1
```

`most_common(1)`만 쓰면 동률을 판별하지 못합니다.
입력 n개에 평균 O(n), 서로 다른 값 u개를 저장하므로 O(u) 공간입니다.
