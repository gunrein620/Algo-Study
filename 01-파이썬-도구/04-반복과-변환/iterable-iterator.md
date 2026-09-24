# 반복 가능한 값과 한 번씩 꺼내는 값

[전체 목차](../../README.md) · [도구 목차](../README.md) · [이 장 목차](README.md)

iterable은 for문으로 순회할 수 있는 객체입니다. list, tuple, str, set, dict, range 등이 해당합니다.
iterator는 다음 원소를 차례로 꺼내며 **소비된 원소를 자동으로 되돌리지 않습니다**.
map, zip, enumerate, reversed의 결과는 iterator입니다. 원본 컬렉션을 변경하지는 않지만,
입력으로 다른 iterator를 주면 그것을 소비합니다. dict를 직접 순회하면 key가 나옵니다.
