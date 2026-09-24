# 조건에 맞는 개수·합 구하기

[전체 목차](../README.md) · [패턴 목차](README.md) · [관련 도구](../01-파이썬-도구/03-리스트/count.md)

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
