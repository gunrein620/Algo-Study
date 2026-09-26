# zip — 같은 위치끼리 묶어서 순회하기

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

두 배열의 같은 위치에 있는 값들을 함께 처리할 때 쓰는 내장함수입니다. import 없이 사용합니다.

```python
absolutes = [4, 7, 12]
signs = [True, False, True]
for num, sign in zip(absolutes, signs):
    print(num, sign)
# 4 True
# 7 False
# 12 True
```

| 반복 | num | sign | 부호 적용 결과 |
| --- | --- | --- | --- |
| 1 | 4 | True | 4 |
| 2 | 7 | False | -7 |
| 3 | 12 | True | 12 |

## 문법과 반환값

`zip(a, b)`는 반복 가능한 입력들을 받아, 같은 위치의 원소를 튜플로 묶어 하나씩 내주는 이터레이터를 반환합니다. 리스트 자체가 필요하면 list로 감쌉니다. 입력 리스트는 변경하지 않습니다.

```python
pairs = list(zip([4, 7, 12], [True, False, True]))
print(pairs)  # [(4, True), (7, False), (12, True)]
```

`for num, sign`은 튜플의 두 값을 각 변수에 나누어 담는 문법입니다.
중첩 for문은 숫자 하나마다 모든 부호를 확인합니다. zip은 같은 위치의 부호만 붙입니다.

## 부호를 적용하고 합산하기

```python
def solution(absolutes, signs):
    answer = []
    for num, sign in zip(absolutes, signs):
        if sign:
            answer.append(num)
        else:
            answer.append(-num)
    return sum(answer)

print(solution([4, 7, 12], [True, False, True]))  # 9
```

append는 `append(값)`으로 호출합니다. `append[값]`이 아닙니다.
같은 풀이를 짧게 쓰면 `sum(num if sign else -num for num, sign in zip(absolutes, signs))`입니다.

## 길이가 다르거나 비어 있다면

기본 zip은 가장 짧은 입력에서 끝납니다. 길이 검사가 필요하면 따로 확인합니다. 음양 더하기는 길이가 같다고 보장합니다.

```python
print(list(zip([1, 2], ['a'])))  # [(1, 'a')]
print(list(zip([], [1])))       # []
pairs = zip([1], ['a'])
print(list(pairs))  # [(1, 'a')]
print(list(pairs))  # []
```

한 번 꺼낸 값은 소비됩니다. `zip(3, [1])`처럼 반복 불가능한 값을 주면 TypeError가 납니다.
인덱스와 값이 필요하면 enumerate, 두 배열의 값이 필요하면 zip입니다.

## reversed — 역순으로 꺼내기

zip과 달리 한 시퀀스를 뒤에서부터 읽는 내장함수입니다. 원본을 변경하지 않고 역순 이터레이터를 반환합니다.

```python
values = [1, 2, 3]
print(list(reversed(values)))  # [3, 2, 1]
print(values)                 # [1, 2, 3]
print(list(reversed([])))      # []
```

일반 제너레이터에는 바로 적용할 수 없습니다(TypeError). 역순의 새 리스트는 `values[::-1]`로도 만들 수 있습니다.

[음양 더하기 오답 기록](../../03-오답노트/2026-09-25-음양-더하기.py) · [이터레이터](iterable-iterator.md)
