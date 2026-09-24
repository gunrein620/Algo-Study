# 정수 제곱근 판별

[전체 목차](../README.md) · [이 폴더 목차](README.md)

정리일: 2026-09-25. 대화에서 확인한 풀이와 설명을 기록합니다. 제출 통과나 독립 재풀이 완료를 의미하지 않습니다.

## 답을 보기 전에

1. isqrt(15)와 isqrt(16)은 각각 무엇일까?
2. isqrt 자체가 제곱수인지 판단해서 bool을 반환할까?

<details>
<summary>내 접근 · 모범답안 · 복습 해설</summary>

isqrt로 후보를 구하고 제곱해서 확인한 첫 풀이가 맞았습니다.

## 모범답안

```python
from math import isqrt

def solution(n):
    x = isqrt(n)
    if x * x == n:
        return (x + 1) ** 2
    return -1

print(solution(121))  # 144
print(solution(3))    # -1
```

isqrt(15)는 3, isqrt(16)은 4입니다. 제곱근을 내린 정수 후보를 반환하므로 x * x == n으로 완전제곱수인지 따로 확인합니다. 첫 풀이의 else도 맞습니다. 앞에서 return하면 함수가 끝나므로 생략할 수 있습니다.

</details>

## 챙길 것

정수 제곱근 후보를 구한 뒤 다시 제곱해서 원래 수와 비교한다.

[isqrt 교과서](../01-파이썬-도구/01-숫자/isqrt.md)

## 재풀이 기록

- [ ] 답을 가리고 직접 작성하기
- [ ] 예제와 경계 입력을 말로 설명하기
- 날짜 / 걸린 시간 / 남은 질문: 미기록
