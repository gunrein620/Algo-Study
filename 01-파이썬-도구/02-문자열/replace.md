# 문자열 바꾸기·지우기 — replace

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

문자열은 불변입니다. 이 메서드는 원본을 직접 바꾸지 않으므로 반환값을 사용합니다.

`s.replace(old, new, count)`는 old를 new로 바꾼 새 str을 반환합니다.
count는 생략하면 전체, 지정하면 최대 그 횟수만큼 앞에서부터 바꿉니다.
삭제할 때는 new로 `""`를 전달합니다. old가 없으면 값이 같은 문자열을 반환합니다.

```python
s = "banana"
assert s.replace("a", "") == "bnn"
assert s.replace("a", "o", 1) == "bonana"
assert s.replace("z", "!") == "banana"
assert s == "banana"
assert "ab".replace("", "-") == "-a-b-"
```

두 번째 인자를 생략하면 삭제가 아니라 TypeError입니다.
