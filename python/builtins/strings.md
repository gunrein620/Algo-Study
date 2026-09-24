# 문자열 메서드

[내장함수 목차](README.md) · [문자열 패턴](../../patterns/strings-arrays.md)

문자열은 immutable(불변)입니다. 아래 메서드는 원본 문자열을 직접 수정하지 않습니다.
새 문자열이 필요하면 반환값을 변수에 저장합니다.

## join — 문자열들을 하나로 합치기

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

## split — 문자열을 조각으로 나누기

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

## replace — 바꾸거나 지우기

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

## isdigit — 숫자 문자인지 판별하기

`s.isdigit()`은 비어 있지 않은 문자열의 모든 문자가 digit인지 bool로 반환합니다.
**정수로 바꾸는 함수가 아닙니다.** 부호나 소수점은 digit이 아닙니다.

```python
assert "123".isdigit() is True
assert "a1".isdigit() is False
assert "-12".isdigit() is False
assert "".isdigit() is False
assert "²".isdigit() is True
```

`int("²")`는 ValueError입니다. Unicode의 digit 범위와 int가 받는 문자열 범위가 같지 않습니다.
문제에서 영문과 0~9만 주어진다면 isdigit을 쓰고, ASCII 숫자만 추출하려면 `"0" <= ch <= "9"`를 씁니다.

## 대소문자 — 변환과 판별

| 메서드 | 반환 | 의미 |
| --- | --- | --- |
| `s.lower()` | str | 소문자로 변환 |
| `s.upper()` | str | 대문자로 변환 |
| `s.swapcase()` | str | 대문자와 소문자 반전 |
| `s.islower()` | bool | 대소문자 구분 문자가 하나 이상 있고 모두 소문자 |
| `s.isupper()` | bool | 대소문자 구분 문자가 하나 이상 있고 모두 대문자 |

```python
s = "Ab1"
assert s.lower() == "ab1"
assert s.upper() == "AB1"
assert s.swapcase() == "aB1"
assert s == "Ab1"
assert "ABC123".isupper() is True
assert "123".isupper() is False
assert "".islower() is False
assert "".lower() == ""
s = s.lower()
assert s == "ab1"
```

영문 문제에서는 직관적으로 사용하면 됩니다. Unicode에서는 대소문자 변환 시 길이가 변할 수도 있습니다.

## 복습

1. `s.lower()`만 호출하면 s가 바뀌는가? → 아니며 재대입이 필요합니다.
2. `"a,,b".split(",")`에서 빈 문자열이 남는 이유는? → 명시한 구분자 사이도 조각입니다.
3. 숫자 리스트를 join하려면? → 각 원소를 str로 변환합니다.
