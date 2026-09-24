# 집계·정렬·탐색

[내장함수 목차](README.md) · [개수와 합 패턴](../../patterns/counting-mapping.md)

## len / sum / min / max — 전체를 요약하기

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

## sorted / list.sort — 새 결과와 원본 변경

| 항목 | `sorted(iterable, key=None, reverse=False)` | `arr.sort(key=None, reverse=False)` |
| --- | --- | --- |
| 종류·입력 | 내장함수, iterable | 리스트 메서드 |
| 반환 | 정렬된 새 `list` | `None` |
| 원본 | 유지 | 직접 변경 |
| 빈 입력 | `[]` | 빈 리스트 유지, None 반환 |

`key`는 비교 기준을 만드는 함수, `reverse=True`는 내림차순입니다.
비교할 수 없는 타입을 섞으면 TypeError가 날 수 있습니다. 같은 key의 원소는 기존 순서를 유지합니다.

```python
arr = [3, 1, 2]
assert sorted(arr) == [1, 2, 3]
assert arr == [3, 1, 2]
result = arr.sort()
assert result is None
assert arr == [1, 2, 3]
assert sorted("bca") == ["a", "b", "c"]
assert "".join(sorted("bca")) == "abc"
assert sorted(["pear", "fig"], key=len) == ["fig", "pear"]
assert sorted(arr, reverse=True) == [3, 2, 1]
```

`arr = arr.sort()`는 arr에 None을 저장하는 실수입니다. n개 정렬은 최악 O(n log n),
sorted는 새 리스트를 만들며 sort도 정렬 중 보조 공간을 사용할 수 있습니다.

## count — 특정 값의 개수

`arr.count(x)`는 리스트에서 x와 같은 값의 수를, `s.count(sub)`는 문자열에서
겹치지 않는 부분 문자열의 출현 횟수를 `int`로 반환합니다. 원본은 유지되고 없으면 0입니다.

```python
assert [1, 1, 2].count(1) == 2
assert [1, 1, 2].count(9) == 0
assert "banana".count("a") == 3
assert "aaaa".count("aa") == 2
assert "abc".count("") == 4  # 문자 앞/사이/뒤의 빈 경계
```

리스트 count는 O(n)입니다. 원소마다 count를 반복하면 O(n²)이 될 수 있으므로 전체 빈도는
[Counter](../standard-library/README.md)를 고려합니다.

## index / find — 값으로 위치 찾기

| 메서드 | 입력 | 반환 | 없는 값 |
| --- | --- | --- | --- |
| `arr.index(x)` | 리스트의 값 x | 첫 위치 `int` | `ValueError` |
| `s.index(sub)` | 부분 문자열 | 첫 위치 `int` | `ValueError` |
| `s.find(sub)` | 부분 문자열 | 첫 위치 `int` | `-1` |

원본은 유지합니다. 리스트에는 find가 없습니다. 문자열 탐색은 선택적으로 start/end를 받으며
end는 미포함이고, 반환 인덱스는 원본 문자열 기준입니다. 빈 문자열은 기본 탐색에서 위치 0에 있습니다.

```python
arr = [7, 5, 3, 5]
assert arr[2] == 3       # 위치 → 값
assert arr.index(3) == 2 # 값 → 첫 위치
assert arr.index(5) == 1
assert "banana".find("na") == 2
assert "banana".find("z") == -1
assert "banana".index("") == 0
```

`if s.find(x):`는 잘못된 판별입니다. 위치 0은 False이고 실패값 -1은 True입니다.
존재 여부만 필요하면 `x in s`, 위치도 필요하면 `pos != -1`을 씁니다.
리스트 index는 최악 O(n)입니다. 빈 리스트에서 index는 ValueError입니다.

## append — 끝에 원소 하나 추가

`arr.append(x)`는 x를 하나의 원소로 추가하는 리스트 메서드입니다. 원본을 변경하고 None을 반환합니다.
괄호로 호출하며 `arr.append[x]`로 쓰지 않습니다. 평균적으로 원소 한 개 추가는 O(1)입니다.

```python
arr = []
assert arr.append(3) is None
assert arr == [3]
arr.append([4, 5])
assert arr == [3, [4, 5]]  # 리스트 전체를 원소 하나로 추가
```

여러 원소를 펼쳐 추가하려면 `arr.extend(iterable)`을 사용합니다(역시 반환값 None).

## 복습

1. `sorted("cab")`의 타입과 값은? → list, `['a', 'b', 'c']`.
2. 없는 값을 찾을 때 -1을 반환하는 것은? → 문자열 find.
3. 원본을 변경하면서 None을 돌려주는 두 메서드는? → sort, append.
