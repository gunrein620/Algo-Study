# 전체 빈도 세기 — Counter

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

`Counter(iterable)`은 원소 → 개수의 Counter 객체(dict의 하위 클래스)를 만듭니다.
원본은 변경하지 않으며 원소는 hashable이어야 합니다. 빈 입력은 빈 Counter,
없는 key 조회는 0입니다. 이건 코테에서 자주 쓰니 챙깁니다.

```python
from collections import Counter
cnt = Counter([1, 1, 2, 3, 3, 3])
assert cnt[3] == 3
assert cnt[9] == 0
assert list(cnt.values()) == [2, 1, 3]
assert list(cnt.items()) == [(1, 2), (2, 1), (3, 3)]
assert cnt.most_common(1) == [(3, 3)]
assert Counter().most_common(1) == []
```

`most_common(k)`는 `(값, 빈도)` tuple들의 list를 반환합니다.
동률은 먼저 나타난 순서입니다. “최빈값 동률이면 -1” 같은 문제 조건을 자동으로 해결하지 않습니다.
길이 n의 입력을 세는 것은 평균 O(n), 서로 다른 값이 u개면 저장 공간 O(u)입니다.
