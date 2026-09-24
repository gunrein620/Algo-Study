# next — 다음 값 하나 꺼내기

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

내장함수이며 import가 필요 없습니다. 지금은 반복문보다 우선해서 외울 도구는 아닙니다. 다른 사람의 짧은 풀이를 읽을 때 알아두면 좋습니다.

## 문법

`next(iterator)` 또는 `next(iterator, 기본값)`으로 사용합니다. 다음 원소 자체를 반환하므로 반환 타입은 원소에 따라 달라집니다.

```python
numbers = iter([2, 3])
print(next(numbers))      # 2
print(next(numbers))      # 3
print(next(numbers, -1))  # -1
```

iter는 리스트 등을 이터레이터로 만듭니다. next는 이터레이터의 진행 위치를 바꿉니다. 원본 리스트의 원소를 삭제하지는 않습니다.
리스트를 바로 `next([2, 3])`에 넣으면 TypeError가 납니다.
다 꺼냈을 때 기본값이 없으면 StopIteration, 기본값이 있으면 그 값을 반환합니다.

## 조건을 만족하는 첫 값

```python
n = 10
answer = next(x for x in range(2, n) if n % x == 1)
print(answer)  # 3
```

2는 조건에 맞지 않아 건너뛰고, 3을 처음 내놓으면 next가 그 값을 꺼냅니다. 안쪽 제너레이터가 조건을 검사하며, next 자체가 검색 조건을 정하는 것은 아닙니다.
이 문제는 n ≥ 3이고 n - 1이 항상 조건을 만족하므로 기본값이 없어도 됩니다.

같은 과정을 익숙한 반복문으로 쓰면 다음과 같습니다.

```python
def solution(n):
    for x in range(2, n):
        if n % x == 1:
            return x

print(solution(10))  # 3
print(solution(12))  # 11
```

한 줄로 줄여도 최악 시간 O(n)은 같습니다. 리스트 컴프리헨션은 결과들을 먼저 저장하지만 제너레이터는 필요한 만큼만 계산합니다.

[컴프리헨션과 제너레이터](../06-문법/comprehension.md)
