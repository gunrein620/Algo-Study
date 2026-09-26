# 빈 값 판별과 or — 결과가 없으면 기본값

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

`a or b`는 a를 참으로 판단하면 a, 거짓으로 판단하면 b를 반환합니다. 실제 피연산자 값을 반환하므로 결과가 항상 bool인 것은 아닙니다.

```python
print([5, 10] or [-1])  # [5, 10]
print([] or [-1])       # [-1]
print(0 or 100)         # 100
print('' or '기본값')   # 기본값
print(3 or 100)         # 3
print(0 or '')          # 빈 문자열: b도 거짓일 수 있음
```

마지막 print는 빈 줄을 출력합니다. a가 거짓이면 b가 참인지와 관계없이 b를 반환합니다.

| 거짓으로 판단하는 대표 값 | 타입 |
| --- | --- |
| False | bool |
| None | NoneType |
| 0, 0.0 | int, float |
| 빈 문자열, 리스트, 튜플, 집합, 딕셔너리 | str, list, tuple, set, dict |

`[-1]`, `[0]`은 원소가 있으므로 참입니다. 문자열 `"False"`도 비어 있지 않아 참입니다.

## 나누어 떨어지는 숫자가 하나도 없다면

```python
def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    return answer or [-1]

print(solution([5, 9, 7, 10], 5))  # [5, 10]
print(solution([3, 2, 6], 10))     # [-1]
```

풀어서 쓰면 `if not answer: return [-1]` 다음에 `return answer`를 쓰는 것과 같습니다.
이 문맥에서 not answer는 빈 리스트인지 확인하고 bool을 반환합니다.

## 기억할 경계

- or는 함수나 메서드가 아닌 연산자입니다. return 없이도 같은 규칙으로 동작합니다.
- a가 참이면 b는 평가하지 않습니다(단락 평가).
- or 자체는 리스트를 복사하거나 수정하지 않습니다. 선택한 객체를 반환합니다.
- 0도 유효한 결과라면 `answer or 기본값`이 의도와 다를 수 있습니다. None만 대체하려면 `기본값 if answer is None else answer`를 씁니다.

[컴프리헨션](comprehension.md) · [나누어 떨어지는 숫자 배열 오답 기록](../../03-오답노트/2026-09-25-나누어-떨어지는-숫자-배열.py)
