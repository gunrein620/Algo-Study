# 값의 위치 찾기 — index와 find

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

| 메서드 | 입력 | 반환 | 없는 값 |
| --- | --- | --- | --- |
| `arr.index(x)` | 리스트의 값 x | 첫 위치 `int` | `ValueError` |
| `s.index(sub)` | 부분 문자열 | 첫 위치 `int` | `ValueError` |
| `s.find(sub)` | 부분 문자열 | 첫 위치 `int` | `-1` |

원본은 유지합니다. 리스트에는 find가 없습니다. 문자열 탐색은 선택적으로 start/end를 받으며
end는 미포함이고, 반환 인덱스는 원본 문자열 기준입니다. 빈 문자열은 기본 탐색에서 위치 0에 있습니다.

```python
arr = [7, 5, 3, 5]
assert arr[2] == 3       # 위치 → 값
assert arr.index(3) == 2 # 값 → 첫 위치
assert arr.index(5) == 1
assert "banana".find("na") == 2
assert "banana".find("z") == -1
assert "banana".index("") == 0
```

`if s.find(x):`는 잘못된 판별입니다. 위치 0은 False이고 실패값 -1은 True입니다.
존재 여부만 필요하면 `x in s`, 위치도 필요하면 `pos != -1`을 씁니다.
리스트 index는 최악 O(n)입니다. 빈 리스트에서 index는 ValueError입니다.
