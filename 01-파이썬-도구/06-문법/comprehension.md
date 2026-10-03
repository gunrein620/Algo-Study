# 컴프리헨션 — 만들기·거르기·값 바꾸기

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

리스트를 만들면서 각 값을 계산하거나 조건에 맞는 값만 담는 문법입니다. 원본 리스트는 바꾸지 않고 새 리스트를 반환합니다.

## 1. 계산한 값을 담기

```python
x, n = 2, 5
answer = [x * i for i in range(1, n + 1)]
print(answer)  # [2, 4, 6, 8, 10]
```

1부터 n까지 반복하며 x * i를 담습니다. `[계산식 for 변수 in 반복할_대상]` 순서로 씁니다.

## 2. 조건에 맞는 원소만 담기 — 뒤쪽 if

```python
arr = [5, 9, 7, 10]
answer = [i for i in arr if i % 5 == 0]
print(answer)  # [5, 10]
```

뒤쪽 if는 담을지 말지를 정합니다. 여기에 else를 붙이지 않습니다.
일반 for문과 연결해서 보면 다음과 같습니다.

```python
arr = [5, 9, 7, 10]
answer = []
for i in arr:
    if i % 5 == 0:
        answer.append(i)
print(answer)  # [5, 10]
```

## 3. 모든 원소를 담되 값을 바꾸기 — 앞쪽 if/else

```python
arr = [5, 9, 7, 10]
answer = [i if i % 5 == 0 else -1 for i in arr]
print(answer)  # [5, -1, -1, 10]
```

| 의도 | 문법 | 결과 원소 수 |
| --- | --- | --- |
| 조건에 맞는 값만 고르기 | `[값 for 값 in 대상 if 조건]` | 줄어들 수 있음 |
| 조건에 따라 넣을 값 선택 | `[A if 조건 else B for 값 in 대상]` | 입력과 같음 |

나누어 떨어지는 숫자 배열 문제는 2번입니다. 결과가 통째로 비었을 때의 처리는 리스트를 만든 뒤 합니다.

```python
arr = [3, 2, 6]
answer = sorted([i for i in arr if i % 10 == 0])
print(answer)         # []
print(answer or [-1]) # [-1]
```

빈 입력으로 리스트 컴프리헨션을 만들면 []입니다. 반복 불가능한 대상을 주면 TypeError가 납니다.

## 제너레이터·집합·딕셔너리로도 만들기

```python
arr = [1, 2, 2, 3, 4]
print(sum(1 for x in arr if x > 2))  # 2: 개수
print(sum(x for x in arr if x > 2))  # 7: 값의 합
print(sorted({x for x in arr}))     # [1, 2, 3, 4]
print({x: x * x for x in [1, 2]})   # {1: 1, 2: 4}
```

`(식 for x in 대상)`은 제너레이터입니다. 필요할 때 하나씩 계산하고 한 번 소비하면 끝납니다. list처럼 모든 값을 먼저 담지 않습니다. 함수의 유일한 인자로 넘길 때는 바깥 괄호 한 쌍을 생략할 수 있습니다.

[빈 결과와 or](truthiness.md) · [next](../04-반복과-변환/next.ipynb)
