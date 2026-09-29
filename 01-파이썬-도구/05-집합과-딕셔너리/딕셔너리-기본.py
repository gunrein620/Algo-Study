# 딕셔너리 — 저장·조회·존재 확인
# 먼저 1~5를 익히고, 그다음 6~8을 읽자.
# 실행: python3 01-파이썬-도구/05-집합과-딕셔너리/딕셔너리-기본.py

# 1. d[키]는 그 키에 연결된 값을 가져온다.
# {}는 빈 딕셔너리(dict). 여기서는 글자(str)를 키, 위치(int)를 값으로 쓴다.
# 값의 타입은 저장한 객체에 따라 달라진다. 조회는 원본을 바꾸지 않는다.
last_seen = {}
print(last_seen)  # {}
last_seen['a'] = 0
print(last_seen)  # {'a': 0}
print(last_seen['a'])  # 0
# last_seen[0]은 역방향 조회가 아니다. 0이라는 키가 없어서 KeyError가 난다.

# 2. 따옴표가 없으면 변수의 값, 있으면 문자열 그대로를 키로 쓴다.
data = {'a': 10, 'ch': 20}
ch = 'a'
print(data[ch])  # 10
print(data['ch'])  # 20
# data[ch]에서 ch를 실제 값으로 바꾸면 data['a']가 된다.

# 3. in은 키의 존재를 검사하고 bool(True/False)을 반환한다.
# 조회도, 존재 확인도 원본을 바꾸지 않는다.
data = {'a': 10}
print('a' in data)  # True
print(10 in data)  # False
print('b' not in data)  # True
print('a' in {})  # False
# 숫자도 키가 될 수 있다. 숫자라서 False인 것은 아니다.
data = {0: 'a'}
print(0 in data)  # True
print(data[0])  # a

# 4. 없는 키에 저장하면 추가, 있는 키에 저장하면 해당 값만 변경한다.
# d[키] = 값은 원본을 변경하는 대입문이다. 같은 키는 둘 생기지 않는다.
data = {'a': 0}
data['b'] = 1
print(data)  # {'a': 0, 'b': 1}
data['a'] = 2
print(data)  # {'a': 2, 'b': 1}
# data = {}를 다시 실행할 때에만 변수 data에 새 빈 딕셔너리를 넣는다.

# 5. 없는 키의 직접 조회는 KeyError. 존재가 불확실하면 먼저 확인한다.
data = {'a': 0}
key = 'b'
if key in data:
    print(data[key])
else:
    print('없음')  # 없음
# print(data['b'])  # 주석을 풀면 KeyError: 'b'가 나고 실행이 멈춘다.
# 빈 딕셔너리도 마찬가지다. 없는 키를 조회해도 -1을 자동 반환하지 않는다.

# 6. enumerate와 연결: idx는 위치(int), ch는 글자(str).
# 딕셔너리가 위치를 알아내는 것이 아니라 우리가 idx를 저장하는 것이다.
last_seen = {}
for idx, ch in enumerate('aba'):
    last_seen[ch] = idx
    print(idx, ch, last_seen)
# 0 a {'a': 0}
# 1 b {'a': 0, 'b': 1}
# 2 a {'a': 2, 'b': 1}
# {}를 반복문 밖에서 만들었으므로 반복이 바뀌어도 앞의 기록이 남는다.
# 빈 문자열이면 반복하지 않아 last_seen은 {} 그대로다.

# 이전 위치를 사용하려면 갱신 전에 꺼낸다.
last_seen = {'a': 0, 'b': 1}
idx = 2
ch = 'a'
previous = last_seen[ch]  # 0: 저장된 이전 위치
print(idx - previous)  # 2: 현재 위치 - 이전 위치
last_seen[ch] = idx
print(last_seen)  # {'a': 2, 'b': 1}
print(previous)  # 0: 따로 저장한 정수는 딕셔너리 갱신으로 바뀌지 않는다.
# 먼저 갱신하고 조회하면 이전 위치도 2가 되어 2 - 2 = 0을 계산하게 된다.

# 7. 값으로 키 찾기: 직접 역조회하지 말고 항목을 확인한다.
# items()는 (키, 값) 쌍을 순회할 수 있는 뷰를 반환한다. 원본 변경 없음.
# 같은 값에 여러 키가 연결될 수 있으므로 결과를 리스트로 모은다.
data = {'a': 10, 'b': 10, 'c': 20}
found = []
for key, value in data.items():
    if value == 10:
        found.append(key)
print(found)  # ['a', 'b']
# 일치하는 값이 없거나 data가 비어 있으면 found는 []다.
# 항목 수가 m개라면 전체 확인에 O(m) 시간이 든다.

# 8. 기본 접근이 익숙해진 뒤 볼 추가 도구
# keys()/values()/items(): 키/값/(키, 값)의 뷰. 원본 변경 없음.
# 뷰는 원본 변경을 반영한다. list(...)로 감싸면 그 시점의 리스트가 된다.
data = {'a': 10, 'b': 20}
print(list(data.keys()))  # ['a', 'b']
print(list(data.values()))  # [10, 20]
print(list(data.items()))  # [('a', 10), ('b', 20)]
print(10 in data.values())  # True: 값 존재 확인. 키를 반환하지는 않는다.
print(list({}.items()))  # []

# get(키, 기본값): 있으면 저장된 값, 없으면 기본값 반환. 원본 변경 없음.
# 기본값을 생략하면 None. 반환 타입은 저장된 값 또는 기본값에 따라 다르다.
print(data.get('a', -1))  # 10
print(data.get('z', -1))  # -1
print(data.get('z'))  # None
print(data)  # {'a': 10, 'b': 20}

# dict.fromkeys(반복 가능한 입력, 값=None): 중복 키를 합친 새 dict 반환.
# 첫 등장 순서를 유지한다. Python 3.7 이상은 삽입 순서를 보장한다.
letters = dict.fromkeys('aba')
print(letters)  # {'a': None, 'b': None}
print(list(letters))  # ['a', 'b']: dict를 순회하면 키가 나온다.
print(dict.fromkeys('', 0))  # {}
# 주의: fromkeys('ab', [])는 두 키가 같은 리스트를 공유한다.
# 키마다 별도 리스트가 필요하면 매번 새 리스트를 만든다.
buckets = {}
for key in 'ab':
    buckets[key] = []
buckets['a'].append(1)
print(buckets)  # {'a': [1], 'b': []}

# 키는 str/int처럼 해시 가능한 값이어야 한다. list/dict는 키로 못 쓴다.
# 값에는 리스트 등도 저장할 수 있다. 같은 값이 여러 번 나와도 된다.
# 키 개수가 m개일 때 조회·저장·in은 평균 O(1), 충돌이 심한 최악에는 O(m).
# 이 파일의 핵심: d[key]는 조회 / d[key] = value는 저장 / key in d는 확인.
