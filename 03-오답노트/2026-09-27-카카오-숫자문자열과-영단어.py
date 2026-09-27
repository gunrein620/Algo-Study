# 카카오 숫자문자열과 영단어
# 막힌 점: 한 글자씩 검사하려 했지만 two/three처럼 첫 글자가 겹친다.
# 단어 길이가 달라 s[::2]로도 나눌 수 없다. 단어 전체를 replace로 바꾸자.
# replace는 새 문자열을 반환한다. s = 로 저장하고, 마지막에 int로 변환한다.


def solution(s):
    words = [
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine'
    ]

    for num, word in enumerate(words):  # (0, 'zero'), (1, 'one'), ...
        s = s.replace(word, str(num))  # 바꿀 값도 문자열이어야 한다.

    return int(s)


# 'one4seveneight' → '14seveneight' → '147eight' → '1478' → 정수 1478
# 같은 단어가 여러 번 나오면 모두 바뀌고, 없는 단어는 그대로 지나간다.
print(solution('one4seveneight'))  # 1478
print(solution('23four5six7'))     # 234567
print(solution('2three45sixseven'))  # 234567
print(solution('123'))            # 123
print(solution('oneone'))         # 11
