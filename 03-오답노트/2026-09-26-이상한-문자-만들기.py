# 이상한 문자 만들기
# 내 실수: s.index(ch)는 현재 위치가 아니라 같은 문자가 처음 나온 위치.
# answer는 단어를 append할 리스트([]), converted는 문자를 붙일 문자열('').


def solution(s):
    answer = []

    for word in s.split(' '):  # 공백으로 나눈 단어가 word에 하나씩 들어온다.
        converted = ''

        # enumerate가 (위치, 문자)를 준다. for문이 각각 idx, ch에 대입한다.
        # 새 word마다 0부터: "try" → (0, 't'), (1, 'r'), (2, 'y')
        for idx, ch in enumerate(word):
            if idx % 2 == 0:
                converted += ch.upper()
            else:
                converted += ch.lower()

        answer.append(converted)

    return ' '.join(answer)  # ' '는 단어 사이에 넣을 구분자.


# split(' ') → 단어별 enumerate → ' '.join()으로 다시 연결
print("hi  you".split(' '))  # ['hi', '', 'you']: 연속 공백 사이에 빈 문자열
# split()은 빈 조각을 없애므로 원래 공백 개수를 복원할 수 없다.
print(' '.join(['Hi', '', 'YoU']))  # Hi  YoU: 빈 조각도 연결해 공백 2개 유지
print(''.join(['TrY', 'HeLlO']))    # TrYHeLlO: 구분자가 없으면 붙음
print(' '.join(['TrY', 'HeLlO']))   # TrY HeLlO: 사이에 공백 하나
print(solution("try hello world"))  # TrY HeLlO WoRlD
