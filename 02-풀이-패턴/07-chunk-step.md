# n개씩 묶기·일정 간격 추출

[전체 목차](../README.md) · [패턴 목차](README.md) · [관련 도구](../01-파이썬-도구/06-문법/slicing.md)

묶음 크기 size는 양수입니다. 인덱스는 size칸씩 이동하고 각 위치에서 size개를 자릅니다.
마지막 묶음이 짧아도 포함합니다.

```python
arr = [1, 2, 3, 4, 5]
size = 2
chunks = [arr[i:i + size] for i in range(0, len(arr), size)]
assert chunks == [[1, 2], [3, 4], [5]]
cipher = "abcdefghi"
code = 3
assert cipher[code - 1::code] == "cfi"
```

i=0 → `[1,2]`, i=2 → `[3,4]`, i=4 → `[5]`입니다.
“3번째 문자”는 인덱스 2이므로 code-1에서 시작합니다. code도 양수여야 합니다.
전체 chunking은 원소 n개를 복사하므로 O(n) 시간·공간입니다.
