# 특정 값의 개수 세기 — count

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

`arr.count(x)`는 리스트에서 x와 같은 값의 수를, `s.count(sub)`는 문자열에서
겹치지 않는 부분 문자열의 출현 횟수를 `int`로 반환합니다. 원본은 유지되고 없으면 0입니다.

```python
assert [1, 1, 2].count(1) == 2
assert [1, 1, 2].count(9) == 0
assert "banana".count("a") == 3
assert "aaaa".count("aa") == 2
assert "abc".count("") == 4  # 문자 앞/사이/뒤의 빈 경계
```

리스트 count는 O(n)입니다. 원소마다 count를 반복하면 O(n²)이 될 수 있으므로 전체 빈도는
[Counter](../05-집합과-딕셔너리/counter.md)를 고려합니다.
