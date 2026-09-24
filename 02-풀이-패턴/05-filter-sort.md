# 문자 필터링·정렬·숫자 추출

[전체 목차](../README.md) · [패턴 목차](README.md) · [관련 도구](../01-파이썬-도구/02-문자열/join.md)

“문자 중 조건에 맞는 것만 남기기”는 순회 → 필터 → join입니다.
정렬 결과는 list이므로 문자열이 필요하면 다시 join합니다.

```python
s = "hello"
assert "".join(ch for ch in s if ch not in "aeiou") == "hll"
assert "".join(sorted("Bca".lower())) == "abc"
s = "a3b1c2"
assert sorted(int(ch) for ch in s if "0" <= ch <= "9") == [1, 2, 3]
assert [int(ch) for ch in sorted(str(3102), reverse=True)] == [3, 2, 1, 0]
assert [len(word) for word in ["hi", "python"]] == [2, 6]
```

숫자 추출은 연속된 수가 아니라 **각 자릿수**를 뽑습니다. `"a12"`라면 `[1, 2]`입니다.
정수 자릿수 정렬 예제는 음이 아닌 정수에 적용합니다(음수의 '-'는 숫자가 아님).
길이 n의 필터링은 O(n), 정렬은 O(n log n), 결과 저장은 O(n)입니다.
