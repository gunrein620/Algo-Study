# 파이썬 도구 — 하고 싶은 일로 찾기

[전체 목차](../README.md) · [함수 이름으로 찾기](함수-찾아보기.md) · [풀이 패턴](../02-풀이-패턴/README.md)

내장함수인지, 메서드인지, import가 필요한지 몰라도 찾을 수 있도록 사용 목적별로 묶었습니다.
각 도구의 상세 문서에서 문법·입력·반환값·예제·주의점을 확인합니다.

## 01. [숫자 계산](01-숫자/README.md)

| 찾는 내용 | 함수·문법 |
| --- | --- |
| [길이·합계·최솟값·최댓값](01-숫자/len-sum-min-max.md) | len · sum · min · max |
| [최대공약수·최소공배수 — gcd와 lcm](01-숫자/gcd-lcm.md) | gcd · lcm |
| [정수 제곱근·제곱수 판별 — isqrt](01-숫자/isqrt.md) | isqrt |
| [정확한 분수 계산 — Fraction](01-숫자/fraction.md) | Fraction |
| [나눗셈·몫·나머지 — /, //, %](01-숫자/division.md) | / · // · % |

## 02. [문자열 다루기](02-문자열/README.md)

| 찾는 내용 | 함수·문법 |
| --- | --- |
| [문자열 합치기 — join](02-문자열/join.md) | join |
| [문자열 나누기 — split](02-문자열/split.md) | split |
| [문자열 바꾸기·지우기 — replace](02-문자열/replace.md) | replace |
| [숫자 문자인지 확인하기 — isdigit](02-문자열/isdigit.md) | isdigit |
| [대소문자 바꾸기·확인하기](02-문자열/case.md) | upper · lower · swapcase · isupper · islower |

## 03. [리스트 다루기](03-리스트/README.md)

| 찾는 내용 | 함수·문법 |
| --- | --- |
| [정렬하기 — sorted와 sort](03-리스트/sorted-sort.md) | sorted · sort |
| [특정 값의 개수 세기 — count](03-리스트/count.md) | count |
| [값의 위치 찾기 — index와 find](03-리스트/index-find.md) | index · find |
| [끝에 원소 추가하기 — append](03-리스트/append.md) | append · extend |

## 04. [반복과 타입 변환](04-반복과-변환/README.md)

| 찾는 내용 | 함수·문법 |
| --- | --- |
| [반복 가능한 값과 한 번씩 꺼내는 값](04-반복과-변환/iterable-iterator.md) | iterable · iterator |
| [정수 범위 반복하기 — range](04-반복과-변환/range.md) | range |
| [인덱스와 값 함께 꺼내기 — enumerate](04-반복과-변환/enumerate.md) | enumerate |
| [각 원소를 같은 함수로 변환하기 — map](04-반복과-변환/map.md) | map |
| [함께 순회하기·역순 순회하기](04-반복과-변환/zip-reversed.md) | zip · reversed |
| [문자·숫자·리스트로 타입 바꾸기](04-반복과-변환/type-conversion.md) | int · str · list · tuple |

## 05. [중복·대응·빈도](05-집합과-딕셔너리/README.md)

| 찾는 내용 | 함수·문법 |
| --- | --- |
| [중복 제거와 집합 연산 — set](05-집합과-딕셔너리/set.md) | set · add |
| [값 대응과 순서 유지 중복 제거 — dict](05-집합과-딕셔너리/dict.md) | dict · fromkeys · get · keys · values · items |
| [전체 빈도 세기 — Counter](05-집합과-딕셔너리/counter.md) | Counter · most_common |

## 06. [Python 문법](06-문법/README.md)

| 찾는 내용 | 함수·문법 |
| --- | --- |
| [컴프리헨션과 제너레이터 표현식](06-문법/comprehension.md) | 컴프리헨션 · 제너레이터 |
| [인덱싱·슬라이싱·뒤집기](06-문법/slicing.md) | 슬라이싱 · [::-1] |
| [두 값 교환하기 — swap](06-문법/swap.md) | swap |

## 읽는 방법

예제의 `assert`는 기대 결과를 확인하는 코드입니다. 오류 없이 실행되면 결과가 일치합니다.
문자열은 원본을 직접 수정할 수 없습니다. 리스트 메서드는 원본 변경 여부를 확인합니다.
예제 기준은 Python 3.9 이상입니다. 실제 제출 환경의 버전도 확인합니다.

[다음에 배울 도구](다음에-배울-도구.md)는 학습 예정 목록입니다.
