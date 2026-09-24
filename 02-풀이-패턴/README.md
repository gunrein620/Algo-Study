# 풀이 패턴 — 문제의 표현으로 찾기

[전체 목차](../README.md) · [파이썬 도구](../01-파이썬-도구/README.md) · [오답노트](../03-오답노트/README.md)

함수 사용법보다 “이 문제를 어떤 흐름으로 풀까?”가 궁금할 때 읽습니다. 각 패턴은 별도 파일입니다.

## 개수·대응·중복

| 하고 싶은 일 | 관련 도구 |
| --- | --- |
| [조건에 맞는 개수·합 구하기](01-count-sum.md) | [count](../01-파이썬-도구/03-리스트/count.md) |
| [고정된 입력을 출력으로 바꾸기](02-mapping.md) | [dict · fromkeys · get · keys · values · items](../01-파이썬-도구/05-집합과-딕셔너리/dict.md) |
| [순서를 유지하며 중복 제거하기](03-deduplicate.md) | [dict · fromkeys · get · keys · values · items](../01-파이썬-도구/05-집합과-딕셔너리/dict.md) |
| [최빈값 구하기 — 동률 처리](04-mode.md) | [Counter · most_common](../01-파이썬-도구/05-집합과-딕셔너리/counter.md) |

## 문자열·리스트

| 하고 싶은 일 | 관련 도구 |
| --- | --- |
| [문자 필터링·정렬·숫자 추출](05-filter-sort.md) | [join](../01-파이썬-도구/02-문자열/join.md) |
| [리스트 한 칸 회전하기](06-rotate.md) | [슬라이싱 · [::-1]](../01-파이썬-도구/06-문법/slicing.md) |
| [n개씩 묶기·일정 간격 추출](07-chunk-step.md) | [슬라이싱 · [::-1]](../01-파이썬-도구/06-문법/slicing.md) |
| [순위 매기기 — 동률과 성능](08-rank.md) | [sorted · sort](../01-파이썬-도구/03-리스트/sorted-sort.md) |
| [음수를 포함한 두 수 곱 최댓값](09-max-product.md) | [sorted · sort](../01-파이썬-도구/03-리스트/sorted-sort.md) |

## 숫자·수학

| 하고 싶은 일 | 관련 도구 |
| --- | --- |
| [자릿수 합·추출·뒤집기](10-digits.md) | [/ · // · %](../01-파이썬-도구/01-숫자/division.md) |
| [약수의 합·개수와 합성수](11-divisors.md) | [isqrt](../01-파이썬-도구/01-숫자/isqrt.md) |
| [최소 묶음 수와 남김없는 분배](12-ceil-lcm.md) | [gcd · lcm](../01-파이썬-도구/01-숫자/gcd-lcm.md) |
| [분수 덧셈과 약분](13-fraction-add.md) | [Fraction](../01-파이썬-도구/01-숫자/fraction.md) |
| [큰 단위부터 최소 개수 구하기](14-greedy-units.md) | [/ · // · %](../01-파이썬-도구/01-숫자/division.md) |
