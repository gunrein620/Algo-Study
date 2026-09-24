# 없는 숫자 더하기

[전체 목차](../README.md) · [이 폴더 목차](README.md)

정리일: 2026-09-25. 대화에서 확인한 풀이와 설명을 기록합니다. 제출 통과나 독립 재풀이 완료를 의미하지 않습니다.

## 답을 보기 전에

1. in과 not in은 무엇을 확인할까?
2. 45에서 입력의 합을 빼도 되는 조건은?

<details>
<summary>내 접근 · 모범답안 · 복습 해설</summary>

0부터 9까지 순회하면서 포함된 수는 continue, 없는 수만 더한 첫 풀이가 맞았습니다.

## 모범답안

```python
def solution(numbers):
    return 45 - sum(numbers)

print(solution([1, 2, 3, 4, 6, 7, 8, 0]))  # 14
print(solution([5, 8, 4, 0, 6, 7, 9]))     # 6
```

0부터 9까지의 전체 합은 45입니다. 첫 예제에서 있는 수의 합은 31이므로 빠진 수의 합은 14입니다.
입력 원소가 모두 0~9이고 서로 다르다는 조건 덕분에 가능합니다. 중복이 있으면 여러 번 빼게 됩니다.
직접 검사하려면 아래와 같이 쓸 수 있습니다.

```python
def solution(numbers):
    answer = 0
    for num in range(10):
        if num not in numbers:
            answer += num
    return answer

print(solution([5, 8, 4, 0, 6, 7, 9]))  # 6
```

`in`은 포함 여부, `not in`은 미포함 여부를 bool로 반환합니다. range(10)은 0~9입니다.
입력 길이 m일 때 sum 풀이는 시간 O(m), 추가 공간 O(1)입니다.

</details>

## 챙길 것

빠진 값의 합 = 전체 합 − 있는 값의 합. 중복 없는 부분집합인지 확인한다.

[빠진 값의 합 패턴](../02-풀이-패턴/15-missing-sum.md)

## 재풀이 기록

- [ ] 답을 가리고 직접 작성하기
- [ ] 예제와 경계 입력을 말로 설명하기
- 날짜 / 걸린 시간 / 남은 질문: 미기록
