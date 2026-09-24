# 04. 문제 풀이 패턴

[전체 목차](../README.md)

문제의 말에서 **필요한 연산**을 찾아 Python 도구로 옮기는 장입니다.
풀이를 암기하기 전에 입력 조건과 결과의 의미를 확인합니다.

| 문제에서 보이는 신호 | 먼저 떠올릴 도구 | 읽을 장 |
| --- | --- | --- |
| 조건을 만족하는 개수 / 합 | sum + 제너레이터 | [집계·매핑·빈도](counting-mapping.md) |
| 입력마다 정해진 출력 | dict 매핑 | [집계·매핑·빈도](counting-mapping.md) |
| 전체 빈도 / 최빈값 | Counter | [집계·매핑·빈도](counting-mapping.md) |
| 중복 제거, 처음 순서 유지 | dict.fromkeys | [집계·매핑·빈도](counting-mapping.md) |
| 문자 제거 / 정렬 / 숫자 추출 | join, sorted, 조건 필터 | [문자열·배열](strings-arrays.md) |
| 회전 / n개씩 묶기 / 일정 간격 | slicing, range | [문자열·배열](strings-arrays.md) |
| 순위 / 음수 포함 곱의 최댓값 | sorted, index, 양 끝 비교 | [문자열·배열](strings-arrays.md) |
| 자릿수 / 몫과 나머지 / 올림 | //, %, str | [수학](math.md) |
| 약수 / 합성수 / 분수 / 같은 분배 | 나머지, gcd, lcm | [수학](math.md) |

패턴은 적용 조건이 맞을 때만 사용합니다. 특히 그리디의 최적성, 순위 동률 규칙, 빈 입력 처리를 확인합니다.
