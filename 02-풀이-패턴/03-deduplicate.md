# 순서를 유지하며 중복 제거하기

[전체 목차](../README.md) · [패턴 목차](README.md) · [관련 도구](../01-파이썬-도구/05-집합과-딕셔너리/dict.md)

“처음 나온 순서대로 한 번씩”이면 `dict.fromkeys`입니다. 단순 set 변환은 입력 순서를 보장하지 않습니다.

```python
s = "people"
assert "".join(dict.fromkeys(s)) == "peol"
```

원리를 풀면 seen에 이미 들어 있는지 확인하는 것입니다.

```python
seen = set()
answer = []
for ch in "people":
    if ch not in seen:
        seen.add(ch)
        answer.append(ch)
assert "".join(answer) == "peol"
```

p, e, o를 추가한 뒤 두 번째 p는 건너뜁니다. l을 추가하고 마지막 e도 건너뜁니다.
길이 n에 평균 O(n) 시간, 서로 다른 원소 u개에 O(u) 공간입니다. 빈 문자열은 빈 문자열이 됩니다.
