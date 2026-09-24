# 순회·변환·컬렉션

[내장함수 목차](README.md) · [문법](../syntax/README.md)

## iterable과 iterator

iterable은 for문으로 순회할 수 있는 객체입니다. list, tuple, str, set, dict, range 등이 해당합니다.
iterator는 다음 원소를 차례로 꺼내며 **소비된 원소를 자동으로 되돌리지 않습니다**.
map, zip, enumerate, reversed의 결과는 iterator입니다. 원본 컬렉션을 변경하지는 않지만,
입력으로 다른 iterator를 주면 그것을 소비합니다. dict를 직접 순회하면 key가 나옵니다.

## range — 정수 범위

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

## enumerate — 인덱스와 값 함께

`enumerate(iterable, start=0)`은 `(번호, 값)` tuple을 내놓는 iterator입니다.
start는 번호의 시작값이며 원소를 건너뛰는 인덱스가 아닙니다. 빈 입력이면 아무 쌍도 만들지 않습니다.

```python
arr = ["a", "b"]
assert list(enumerate(arr)) == [(0, "a"), (1, "b")]
assert list(enumerate(arr, start=1)) == [(1, "a"), (2, "b")]
for idx, value in enumerate(arr):
    assert arr[idx] == value
```

## map — 원소마다 같은 함수 적용

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

## zip / reversed — 묶거나 역순으로 순회

`zip(a, b)`는 같은 위치의 원소들을 tuple로 묶은 iterator를 반환합니다.
기본 동작은 가장 짧은 입력에서 끝납니다. 빈 입력이 하나라도 있으면 결과는 비어 있습니다.
`reversed(sequence)`는 역순 iterator를 반환합니다. 일반 제너레이터에는 바로 적용할 수 없습니다.

```python
assert list(zip([1, 2], ["a"])) == [(1, "a")]
assert list(zip([], [1])) == []
assert list(reversed([1, 2, 3])) == [3, 2, 1]
```

리스트를 뒤집은 새 리스트가 필요하면 `arr[::-1]`도 가능합니다.

## int / str / list / tuple — 타입 바꾸기

| 내장 타입 생성자 | 입력 → 반환 | 주의 |
| --- | --- | --- |
| `int(x)` | 정수 문자열/수 → int | 잘못된 문자열은 ValueError; 실수는 0 방향으로 절삭 |
| `str(x)` | 객체 → str | 숫자도 문자로 변환 |
| `list(iterable)` | iterable → list | 원소는 얕게 복사; 인자 없으면 [] |
| `tuple(iterable)` | iterable → tuple | 변경 불가능한 순서열; 인자 없으면 () |

```python
assert int("-123") == -123
assert str(123) == "123"
assert "1" != 1
assert list("abc") == ["a", "b", "c"]
assert tuple([1, 2]) == (1, 2)
assert int(-3.9) == -3
```

## set — 중복 제거와 집합 연산

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

## dict / dict.fromkeys — 대응과 순서 유지 중복 제거

`dict`는 key → value 대응을 저장합니다. key는 hashable이어야 하며 중복 key는 하나만 남습니다.
`d[key]`는 없으면 KeyError, `d.get(key, default)`는 없으면 default(생략 시 None)를 반환합니다.
`keys()`, `values()`, `items()`는 각각 key, 값, `(key, value)`의 동적 view를 반환합니다.

`dict.fromkeys(iterable, value=None)`는 처음 등장한 순서대로 key를 넣은 새 dict를 만듭니다.
빈 입력은 `{}`입니다. Python 3.7 이상에서 dict의 삽입 순서는 언어 차원에서 보장됩니다.

```python
d = dict.fromkeys("people")
assert list(d) == ["p", "e", "o", "l"]
assert "".join(d) == "peol"
assert list(d.values()) == [None, None, None, None]
assert d.get("z", 0) == 0
assert list(dict.fromkeys([3, 1, 3])) == [3, 1]
```

value에 `[]` 같은 변경 가능한 객체를 넣으면 모든 key가 **같은 객체**를 공유합니다.
각 key에 별도 리스트가 필요하면 `{key: [] for key in keys}`를 씁니다.
순서 유지 중복 제거는 [패턴 장](../../patterns/counting-mapping.md)에서 복습합니다.
