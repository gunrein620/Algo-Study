# 집계·매핑·빈도

[패턴 목차](README.md) · [함수 설명](../python/builtins/aggregation-search.md)

## 조건 만족 개수와 값의 합

“키가 height보다 큰 사람 수”는 조건을 통과할 때마다 **1**을 더합니다.
“그 사람들의 키 합”은 실제 값 x를 더합니다. 입력 n개에 O(n) 시간, 제너레이터 자체는 O(1) 추가 공간입니다.

```python
arr = [150, 180, 170]
height = 160
assert sum(1 for x in arr if x > height) == 2
assert sum(x for x in arr if x > height) == 350
```

일반 반복문으로 읽으면 다음과 같습니다.

```python
arr = [150, 180, 170]
count = 0
for x in arr:
    if x > 160:
        count += 1
assert count == 2
```

150은 건너뛰고, 180에서 1, 170에서 2가 됩니다. 빈 입력의 합과 개수는 모두 0입니다.
특정 값 하나의 개수만 세면 `arr.count(value)`가 더 직접적입니다.
평균은 `sum(arr) / len(arr)`이며 빈 입력을 제외하거나 별도 처리해야 합니다.

## 고정 대응은 dict

가위바위보처럼 입력 하나에 출력 하나가 정해져 있으면 조건문을 여러 번 쓰는 대신 대응표를 만듭니다.
아래 문제의 기호는 2=가위, 0=바위, 5=보라고 가정합니다.

```python
win = {"2": "0", "0": "5", "5": "2"}
rsp = "205"
assert "".join(win[ch] for ch in rsp) == "052"
```

2 → 0, 0 → 5, 5 → 2를 연결합니다. 정의되지 않은 기호는 KeyError입니다.
길이 n에 평균 O(n) 시간과 O(n) 결과 공간입니다.

## 순서 유지 중복 제거

“처음 나온 순서대로 한 번씩”이면 `dict.fromkeys`입니다. 단순 set 변환은 입력 순서를 보장하지 않습니다.

```python
s = "people"
assert "".join(dict.fromkeys(s)) == "peol"
```

원리를 풀면 seen에 이미 들어 있는지 확인하는 것입니다.

```python
seen = set()
answer = []
for ch in "people":
    if ch not in seen:
        seen.add(ch)
        answer.append(ch)
assert "".join(answer) == "peol"
```

p, e, o를 추가한 뒤 두 번째 p는 건너뜁니다. l을 추가하고 마지막 e도 건너뜁니다.
길이 n에 평균 O(n) 시간, 서로 다른 원소 u개에 O(u) 공간입니다. 빈 문자열은 빈 문자열이 됩니다.

## 최빈값 — 동률 조건까지 처리

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

## 가져갈 것

- 개수는 1을 더하고, 합은 값을 더합니다.
- 고정 대응은 dict, 전체 빈도는 Counter입니다.
- 중복을 제거할 때 순서가 필요한지 먼저 확인합니다.

복습: “조건 만족 값의 리스트”가 필요하면? → `[x for x in arr if 조건]`.
