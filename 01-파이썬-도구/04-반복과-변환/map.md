# 각 원소를 같은 함수로 변환하기 — map

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

`map(function, iterable)`은 변환 결과를 차례로 내놓는 map iterator입니다.
리스트가 필요하면 list로 감쌉니다. 실제 변환은 소비할 때 진행되므로 잘못된 값의 예외도 그때 발생합니다.
빈 입력은 소비해도 빈 결과입니다.

```python
converted = map(int, ["1", "2", "3"])
assert list(converted) == [1, 2, 3]
assert list(converted) == []  # 이미 소비함
assert [int(x) for x in ["1", "2"]] == [1, 2]
```

단순 함수 적용에는 map, 조건이나 계산식이 추가되면 컴프리헨션이 읽기 좋습니다.

관련 개념: [iterable과 iterator — 반복과 소비의 차이](iterable-iterator.md).
