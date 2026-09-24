# 문자열 합치기 — join

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

문자열은 불변입니다. 이 메서드는 원본을 직접 바꾸지 않으므로 반환값을 사용합니다.

문법은 `구분자.join(iterable)`입니다. iterable의 **모든 원소가 str**여야 하며 결과는 str입니다.
빈 iterable은 `""`를 반환합니다. 숫자를 섞으면 TypeError이므로 먼저 str로 변환합니다.

```python
assert "".join(["a", "b", "c"]) == "abc"
assert "-".join(["a", "b"]) == "a-b"
assert "".join([]) == ""
assert ",".join(map(str, [1, 2])) == "1,2"
```

`''.join(ch for ch in s if 조건)`은 조건에 맞는 문자만 합치는 대표 패턴입니다.
결과 총 길이 L과 원소 수 k에 대해 대략 O(L+k)의 작업이 필요합니다.
