# 순위 매기기 — 동률과 성능

[전체 목차](../README.md) · [패턴 목차](README.md) · [관련 도구](../01-파이썬-도구/03-리스트/sorted-sort.md)

아래는 내림차순에서 첫 위치+1을 사용하는 **공동 순위 후 건너뛰기** 규칙입니다.
예를 들어 `[7,7,5]`는 `[1,1,3]`입니다. 문제의 동률 규칙을 먼저 확인합니다.

```python
emergency = [3, 7, 5]
sorted_arr = sorted(emergency, reverse=True)
answer = [sorted_arr.index(value) + 1 for value in emergency]
assert sorted_arr == [7, 5, 3]
assert answer == [3, 1, 2]
```

처음 value=3의 위치는 2 → 3등, 다음 7의 위치는 0 → 1등, 마지막 5는 1 → 2등입니다.
index를 n번 호출하면 O(n²)이므로 작은 입력에서 개념을 익히는 풀이입니다.
같은 순위 규칙을 큰 입력에 적용할 때는 최초 등수를 dict에 저장합니다.

```python
emergency = [7, 7, 5]
ranks = {}
for rank, value in enumerate(sorted(emergency, reverse=True), start=1):
    if value not in ranks:
        ranks[value] = rank
assert [ranks[value] for value in emergency] == [1, 1, 3]
```

정렬 O(n log n), dict 저장·조회 평균 O(n), 추가 공간 O(n)입니다.
