# 문자열 나누기 — split

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

문자열은 불변입니다. 이 메서드는 원본을 직접 바꾸지 않으므로 반환값을 사용합니다.

`s.split(sep=None, maxsplit=-1)`은 `list[str]`를 반환합니다.
구분자를 생략하면 연속 공백을 하나의 경계로 처리합니다. 명시한 구분자는 그대로 적용합니다.
구분자가 없으면 원래 문자열 하나가 담긴 리스트가 나오고, sep가 빈 문자열이면 ValueError입니다.

```python
assert "  10  20\n".split() == ["10", "20"]
assert "a,,b".split(",") == ["a", "", "b"]
assert "".split() == []
assert "".split(",") == [""]
assert "a,b,c".split(",", 1) == ["a", "b,c"]
assert list(map(int, "10 20 30".split())) == [10, 20, 30]
```

입력 한 줄을 정수 리스트로 받을 때는 `list(map(int, input().split()))`을 사용합니다.
join은 조각을 합치고 split은 조각으로 나눕니다.
