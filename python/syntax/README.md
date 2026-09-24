# 02. 문법과 연산자

[전체 목차](../../README.md)

## /, //, % — 나누기, 몫, 나머지

정수 7과 2에 대해 `/`는 3.5, `//`는 3, `%`는 1입니다.
0으로 나누면 ZeroDivisionError입니다. 정수의 `//`는 아래쪽 정수로 내리므로 음수에서 주의합니다.

```python
assert 7 / 2 == 3.5
assert 7 // 2 == 3
assert 7 % 2 == 1
assert -7 // 2 == -4
assert -7 % 2 == 1
assert 6 % 3 == 0  # 6은 3의 배수, 3은 6의 약수
assert 3 % 6 == 3  # 순서를 바꾸면 의미도 달라짐
```

양의 정수 a, b에서 필요한 묶음 수는 `(a + b - 1) // b`입니다(a=0도 가능).
예를 들어 10명을 한 판 7조각 피자로 먹이려면 `(10 + 6) // 7 == 2`판입니다.

## 컴프리헨션과 제너레이터 표현식

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

## 슬라이싱 — start 포함, end 미포함

`arr[start:end:step]`은 지정한 구간을 추출합니다. 리스트는 새 리스트(얕은 복사), 문자열은 문자열입니다.
범위를 넘어가는 슬라이스는 잘라서 처리하지만, 단일 인덱싱은 범위를 벗어나면 IndexError입니다.
step은 0일 수 없습니다. 음수 step에서는 진행 방향도 반대입니다.

```python
arr = [1, 2, 3, 4, 5]
assert arr[1:4] == [2, 3, 4]
assert arr[:3] == [1, 2, 3]
assert arr[2:] == [3, 4, 5]
assert arr[:] == [1, 2, 3, 4, 5]
assert arr[::2] == [1, 3, 5]
assert arr[::-1] == [5, 4, 3, 2, 1]
assert arr[:-1] == [1, 2, 3, 4]
assert arr[-1:] == [5]
assert arr[99:] == []
assert [][-1:] == []
```

`arr[-1]`은 마지막 **값** 5, `arr[-1:]`은 마지막 원소를 담은 **리스트** `[5]`입니다.
추출 길이가 k인 리스트/문자열 슬라이스는 일반적으로 O(k) 시간과 결과 공간이 필요합니다.
회전, 묶음 자르기, 일정 간격 추출은 [배열 패턴](../../patterns/strings-arrays.md)에서 다룹니다.

## swap과 문자열 수정

Python은 `a, b = b, a`로 교환합니다. 오른쪽 값을 먼저 평가하고 왼쪽에 대입합니다.
문자열의 개별 위치는 수정할 수 없으므로 리스트로 변환하고 마지막에 join합니다.

```python
arr = list("abc")
arr[0], arr[2] = arr[2], arr[0]
assert "".join(arr) == "cba"
```

## 복습

1. `sum(1 for ...)`의 1을 x로 바꾸면? → 개수가 아니라 값의 합.
2. `[1, 2, 3][1:3]`에 인덱스 3이 포함되는가? → 미포함, 결과 `[2, 3]`.
3. `-7 // 2`가 -3이 아닌 이유는? → 아래쪽 정수로 내리기 때문.
