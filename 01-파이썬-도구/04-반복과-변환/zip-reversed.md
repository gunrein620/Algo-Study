# 함께 순회하기·역순 순회하기

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

`zip(a, b)`는 같은 위치의 원소들을 tuple로 묶은 iterator를 반환합니다.
기본 동작은 가장 짧은 입력에서 끝납니다. 빈 입력이 하나라도 있으면 결과는 비어 있습니다.
`reversed(sequence)`는 역순 iterator를 반환합니다. 일반 제너레이터에는 바로 적용할 수 없습니다.

```python
assert list(zip([1, 2], ["a"])) == [(1, "a")]
assert list(zip([], [1])) == []
assert list(reversed([1, 2, 3])) == [3, 2, 1]
```

리스트를 뒤집은 새 리스트가 필요하면 `arr[::-1]`도 가능합니다.

관련 개념: [iterable과 iterator — 반복과 소비의 차이](iterable-iterator.md).
