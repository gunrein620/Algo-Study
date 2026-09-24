# 컴프리헨션과 제너레이터 표현식

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

| 문법 | 결과 | 용도 |
| --- | --- | --- |
| `[식 for x in iterable if 조건]` | list | 순서대로 변환·필터링 |
| `{식 for x in iterable if 조건}` | set | 중복 없이 수집 |
| `{key: value for x in iterable}` | dict | 대응 관계 생성 |
| `(식 for x in iterable if 조건)` | generator | 필요할 때 하나씩 계산 |

```python
arr = [1, 2, 2, 3, 4]
assert [x * 2 for x in arr] == [2, 4, 4, 6, 8]
assert [x for x in arr if x % 2 == 0] == [2, 2, 4]
assert {x for x in arr} == {1, 2, 3, 4}
assert {x: x * x for x in [1, 2]} == {1: 1, 2: 4}
assert sum(1 for x in arr if x > 2) == 2
assert sum(x for x in arr if x > 2) == 7
```

마지막 두 줄은 **개수**와 **실제 값의 합**이라는 차이가 있습니다.
제너레이터는 한 번 소비하면 끝이며, 리스트처럼 모든 결과를 먼저 저장하지 않습니다.

한 줄이 낯설면 다음 순서로 읽습니다: 반복 → 조건 검사 → 결과에 식 추가.

```python
arr = [1, 2, 3, 4]
answer = []
for x in arr:
    if x % 2 == 0:
        answer.append(x)
assert answer == [2, 4]
```

x는 1 → 2 → 3 → 4로 바뀝니다. 조건을 통과한 2, 4만 answer에 들어갑니다.
