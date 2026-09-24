# 문자열·배열 패턴

[패턴 목차](README.md) · [문자열 도구](../python/builtins/strings.md) · [슬라이싱](../python/syntax/README.md)

## 문자열 필터링·정렬·숫자 추출

“문자 중 조건에 맞는 것만 남기기”는 순회 → 필터 → join입니다.
정렬 결과는 list이므로 문자열이 필요하면 다시 join합니다.

```python
s = "hello"
assert "".join(ch for ch in s if ch not in "aeiou") == "hll"
assert "".join(sorted("Bca".lower())) == "abc"
s = "a3b1c2"
assert sorted(int(ch) for ch in s if "0" <= ch <= "9") == [1, 2, 3]
assert [int(ch) for ch in sorted(str(3102), reverse=True)] == [3, 2, 1, 0]
assert [len(word) for word in ["hi", "python"]] == [2, 6]
```

숫자 추출은 연속된 수가 아니라 **각 자릿수**를 뽑습니다. `"a12"`라면 `[1, 2]`입니다.
정수 자릿수 정렬 예제는 음이 아닌 정수에 적용합니다(음수의 '-'는 숫자가 아님).
길이 n의 필터링은 O(n), 정렬은 O(n log n), 결과 저장은 O(n)입니다.

## 한 칸 회전

오른쪽 회전은 마지막 조각 + 나머지, 왼쪽 회전은 나머지 + 첫 조각입니다.
단일 인덱싱 대신 슬라이싱을 쓰면 빈 리스트도 안전합니다.

```python
arr = [1, 2, 3, 4]
assert arr[-1:] + arr[:-1] == [4, 1, 2, 3]
assert arr[1:] + arr[:1] == [2, 3, 4, 1]
arr = []
assert arr[-1:] + arr[:-1] == []
```

길이 n에 O(n) 시간·공간입니다. 반복 회전이 많다면 deque 등 다른 표현을 고려합니다.

## n개씩 자르기와 일정 간격 추출

묶음 크기 size는 양수입니다. 인덱스는 size칸씩 이동하고 각 위치에서 size개를 자릅니다.
마지막 묶음이 짧아도 포함합니다.

```python
arr = [1, 2, 3, 4, 5]
size = 2
chunks = [arr[i:i + size] for i in range(0, len(arr), size)]
assert chunks == [[1, 2], [3, 4], [5]]
cipher = "abcdefghi"
code = 3
assert cipher[code - 1::code] == "cfi"
```

i=0 → `[1,2]`, i=2 → `[3,4]`, i=4 → `[5]`입니다.
“3번째 문자”는 인덱스 2이므로 code-1에서 시작합니다. code도 양수여야 합니다.
전체 chunking은 원소 n개를 복사하므로 O(n) 시간·공간입니다.

## 순위 — 위치는 0부터, 등수는 1부터

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

## 두 수 곱 최댓값 — 음수가 있으면 양 끝

서로 다른 위치의 두 원소를 골라 곱합니다. 입력은 적어도 두 개의 수를 포함해야 합니다.
정렬 후 가장 작은 두 수의 곱과 가장 큰 두 수의 곱을 비교합니다.

```python
numbers = sorted([-10, -9, 1, 2, 3])
answer = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
assert answer == 90
```

음수 둘의 곱이 양수가 되므로 오른쪽 끝 두 개만 확인하면 놓칠 수 있습니다.
정렬을 쓰므로 O(n log n) 시간, sorted의 결과 공간 O(n)입니다.

## 가져갈 것

- 문자열 결과가 필요하면 sorted/필터 결과를 join합니다.
- 슬라이싱의 끝은 미포함이며, “몇 번째”는 인덱스로 바꾸어 생각합니다.
- 순위의 동률과 음수 곱처럼 문제 조건이 풀이를 바꾸는지 확인합니다.

복습: `[1,2,3,4,5]`를 size=3으로 자르면? → `[[1,2,3],[4,5]]`.
