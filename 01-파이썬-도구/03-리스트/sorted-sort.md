# 정렬하기 — sorted와 sort

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

| 항목 | `sorted(iterable, key=None, reverse=False)` | `arr.sort(key=None, reverse=False)` |
| --- | --- | --- |
| 종류·입력 | 내장함수, iterable | 리스트 메서드 |
| 반환 | 정렬된 새 `list` | `None` |
| 원본 | 유지 | 직접 변경 |
| 빈 입력 | `[]` | 빈 리스트 유지, None 반환 |

`key`는 비교 기준을 만드는 함수, `reverse=True`는 내림차순입니다.
비교할 수 없는 타입을 섞으면 TypeError가 날 수 있습니다. 같은 key의 원소는 기존 순서를 유지합니다.

```python
arr = [3, 1, 2]
assert sorted(arr) == [1, 2, 3]
assert arr == [3, 1, 2]
result = arr.sort()
assert result is None
assert arr == [1, 2, 3]
assert sorted("bca") == ["a", "b", "c"]
assert "".join(sorted("bca")) == "abc"
assert sorted(["pear", "fig"], key=len) == ["fig", "pear"]
assert sorted(arr, reverse=True) == [3, 2, 1]
```

`arr = arr.sort()`는 arr에 None을 저장하는 실수입니다. n개 정렬은 최악 O(n log n),
sorted는 새 리스트를 만들며 sort도 정렬 중 보조 공간을 사용할 수 있습니다.
