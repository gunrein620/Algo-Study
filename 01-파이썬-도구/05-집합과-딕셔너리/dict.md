# 값 대응과 순서 유지 중복 제거 — dict

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

`dict`는 key → value 대응을 저장합니다. key는 hashable이어야 하며 중복 key는 하나만 남습니다.
`d[key]`는 없으면 KeyError, `d.get(key, default)`는 없으면 default(생략 시 None)를 반환합니다.
`keys()`, `values()`, `items()`는 각각 key, 값, `(key, value)`의 동적 view를 반환합니다.

`dict.fromkeys(iterable, value=None)`는 처음 등장한 순서대로 key를 넣은 새 dict를 만듭니다.
빈 입력은 `{}`입니다. Python 3.7 이상에서 dict의 삽입 순서는 언어 차원에서 보장됩니다.

```python
d = dict.fromkeys("people")
assert list(d) == ["p", "e", "o", "l"]
assert "".join(d) == "peol"
assert list(d.values()) == [None, None, None, None]
assert d.get("z", 0) == 0
assert list(dict.fromkeys([3, 1, 3])) == [3, 1]
```

value에 `[]` 같은 변경 가능한 객체를 넣으면 모든 key가 **같은 객체**를 공유합니다.
각 key에 별도 리스트가 필요하면 `{key: [] for key in keys}`를 씁니다.
순서 유지 중복 제거는 [패턴 장](../../02-풀이-패턴/03-deduplicate.md)에서 복습합니다.
