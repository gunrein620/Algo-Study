# 음수를 포함한 두 수 곱 최댓값

[전체 목차](../README.md) · [패턴 목차](README.md) · [관련 도구](../01-파이썬-도구/03-리스트/sorted-sort.md)

서로 다른 위치의 두 원소를 골라 곱합니다. 입력은 적어도 두 개의 수를 포함해야 합니다.
정렬 후 가장 작은 두 수의 곱과 가장 큰 두 수의 곱을 비교합니다.

```python
numbers = sorted([-10, -9, 1, 2, 3])
answer = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
assert answer == 90
```

음수 둘의 곱이 양수가 되므로 오른쪽 끝 두 개만 확인하면 놓칠 수 있습니다.
정렬을 쓰므로 O(n log n) 시간, sorted의 결과 공간 O(n)입니다.
