# 끝에 원소 추가하기 — append

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

`arr.append(x)`는 x를 하나의 원소로 추가하는 리스트 메서드입니다. 원본을 변경하고 None을 반환합니다.
괄호로 호출하며 `arr.append[x]`로 쓰지 않습니다. 평균적으로 원소 한 개 추가는 O(1)입니다.

```python
arr = []
assert arr.append(3) is None
assert arr == [3]
arr.append([4, 5])
assert arr == [3, [4, 5]]  # 리스트 전체를 원소 하나로 추가
```

여러 원소를 펼쳐 추가하려면 `arr.extend(iterable)`을 사용합니다(역시 반환값 None).
