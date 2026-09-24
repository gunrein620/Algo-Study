# 05. 실수와 복습노트

[전체 목차](../README.md) · [문제 기록 양식](problem-template.md)

아래는 이전 학습 맥락에서 반복했던 실수입니다. 매 문제마다 전부 외우기보다 지금 코드에 해당하는 것만 확인합니다.

## 문제별 복습 기록

리뷰의 질문부터 답하고, 막힌 문법은 연결된 교과서에서 확인합니다.

| 기록일 | 문제 | 다시 볼 지점 | 상태 |
| --- | --- | --- | --- |
| 2026-09-24 | [자연수 뒤집어 배열로 만들기](2026-09-24-reverse-digits.md) | 정렬과 뒤집기 구분, 함수 반환값에 슬라이싱 | 설명 확인, 독립 재풀이 미확인 |

## 실수 점검표

| 실수 | 바르게 생각하기 | 복습 |
| --- | --- | --- |
| 리스트를 `range(arr)`에 넣음 | 값 순회는 `for x in arr`, 인덱스는 `range(len(arr))` | [순회](../python/builtins/iteration-collections.md) |
| `arr.append[x]` | 메서드 호출은 `arr.append(x)` | [append](../python/builtins/aggregation-search.md) |
| `return print(answer)` | print의 반환은 None; 프로그래머스 solution은 `return answer` | 아래 회상 질문 |
| `money - 5500`만 씀 | 저장하려면 `money -= 5500` | 아래 회상 질문 |
| 할인 조건을 작은 기준부터 검사 | `>= 500000`, `>= 300000`, `>= 100000` 순서 | 아래 회상 질문 |
| sorted 결과를 문자열로 생각 | 결과는 list, 필요하면 join | [정렬](../python/builtins/aggregation-search.md) |
| lower/replace가 원본을 바꾼다고 생각 | 새 문자열을 반환; 필요하면 재대입 | [문자열](../python/builtins/strings.md) |
| `for ch in s`의 ch를 인덱스로 생각 | ch는 문자; 둘 다 필요하면 enumerate | [순회](../python/builtins/iteration-collections.md) |
| `arr[i]`와 `arr.index(x)` 혼동 | 위치 → 값 / 값 → 첫 위치 | [탐색](../python/builtins/aggregation-search.md) |
| `"1"`과 `1`을 같은 값으로 생각 | str와 int를 구분 | [형변환](../python/builtins/iteration-collections.md) |

## 5분 회상 연습

정답을 보기 전에 말로 설명하고 한 줄 코드를 직접 작성합니다.

1. `arr = [7,5,3]`에서 값 3의 위치와 위치 2의 값을 각각 구하기.
2. `"people"`에서 처음 등장한 순서를 유지하며 중복 제거하기.
3. `[1,4,7]`에서 3보다 큰 값의 개수와 합 구하기.
4. `"abcdefghi"`에서 세 번째 문자부터 세 칸마다 추출하기.
5. `print`와 `return`이 다른 이유 설명하기.
6. `money - 5500`만 쓰면 money가 바뀌는지 설명하기.
7. 50만원 이상 20%, 30만원 이상 10% 할인에서 작은 기준부터 검사하면 생기는 문제 설명하기.

<details>
<summary>정답 확인</summary>

1. `arr.index(3) == 2`, `arr[2] == 3`.
2. `''.join(dict.fromkeys("people")) == "peol"`.
3. `sum(1 for x in arr if x > 3)`은 2, `sum(x for x in arr if x > 3)`은 11.
4. `s[2::3] == "cfi"`.
5. print는 화면 출력이며 반환값은 None. return은 함수의 결과를 호출자에게 전달.
6. 계산만 하며 저장하지 않음. `money -= 5500` 또는 `money = money - 5500` 필요.
7. if/elif에서 50만원도 먼저 30만원 조건을 통과해 10% 할인이 적용될 수 있음.

</details>

## 복습 운영

- 당일: 문제 기록 양식에 내 접근, 수정 이유, 가져갈 것 1~3개를 작성합니다.
- 다음 날: 모범답안을 가리고 핵심 구현을 다시 작성합니다.
- 일주일 뒤: 비슷한 문제에서 같은 도구를 스스로 선택하는지 확인합니다.
- 실제로 풀지 않은 문제를 완료 처리하지 않습니다. 도움 없이 구현했는지 구분합니다.
