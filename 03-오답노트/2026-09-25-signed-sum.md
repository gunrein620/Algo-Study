# 음양 더하기 — 같은 위치끼리 짝짓기

[전체 목차](../README.md) · [이 폴더 목차](README.md)

정리일: 2026-09-25. 대화에서 확인한 풀이와 설명을 기록합니다. 제출 통과나 독립 재풀이 완료를 의미하지 않습니다.

## 답을 보기 전에

1. 중첩 for문과 zip은 숫자와 부호를 어떻게 다르게 연결할까?
2. sign이 True이면 양수일까, 음수일까?
3. `answer.append[-num]`이 안 되는 이유는?

<details>
<summary>내 접근 · 모범답안 · 복습 해설</summary>

## 내 시도에서 막힌 부분

처음에는 숫자 하나마다 모든 부호를 반복했고, 참인 부호에서 음수를 넣은 뒤 양수도 무조건 추가했습니다.
zip으로 바꾼 뒤에는 짝짓기와 부호 처리는 맞았지만 `answer.append[-num]`으로 작성했습니다.

| 시도 | 수정과 이유 |
| --- | --- |
| 숫자 for문 안에 부호 for문 | 같은 인덱스끼리 처리하도록 zip 사용 |
| True에서 음수로 변환 | True는 양수 유지, False는 음수 |
| 음수 처리 후 양수도 추가 | if/else로 하나만 추가 |
| `num - num * 2` | 같은 값인 `-num`으로 표현 |
| `answer.append[-num]` | 메서드 실행은 `answer.append(-num)` |

## 내가 고친 흐름을 완성한 풀이

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
print(solution([1, 2, 3], [False, False, True]))  # 0
```

`(4, True) → 4`, `(7, False) → -7`, `(12, True) → 12`이므로 리스트는 `[4, -7, 12]`입니다.
`if sign:`으로 bool을 바로 검사합니다. True == 1은 Python에서 참이지만 부호 변수는 그대로 검사하는 편이 명확합니다.

## 짧은 모범답안

```python
def solution(absolutes, signs):
    return sum(num if sign else -num
               for num, sign in zip(absolutes, signs))

print(solution([4, 7, 12], [True, False, True]))  # 9
```

길이가 m일 때 두 풀이 모두 시간 O(m). 리스트 풀이의 추가 공간은 O(m), 제너레이터 풀이의 추가 공간은 O(1)입니다.

</details>

## 챙길 것

1. 같은 위치의 두 값은 zip으로 묶는다.
2. `리스트[위치]`는 원소 접근, `append(값)`은 메서드 호출이다.

[zip 교과서](../01-파이썬-도구/04-반복과-변환/zip-reversed.md) · [append](../01-파이썬-도구/03-리스트/append.md)

## 재풀이 기록

- [ ] 답을 가리고 직접 작성하기
- [ ] 예제와 경계 입력을 말로 설명하기
- 날짜 / 걸린 시간 / 남은 질문: 미기록
