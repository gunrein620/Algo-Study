# 문자열 내 p와 y의 개수
# 내 첫 풀이도 정답: p/P, y/Y를 각각 세고 두 개수를 비교했다.
# lower로 소문자로 통일하면 대소문자를 따로 검사할 필요가 없다.
# lower는 새 문자열을 반환하므로 s에 다시 저장한다.


def my_solution(s):
    cnt_p = 0
    cnt_y = 0
    for ch in s:
        if ch == 'p' or ch == 'P':
            cnt_p += 1
        if ch == 'y' or ch == 'Y':
            cnt_y += 1
    return cnt_p == cnt_y


def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')


print(solution("pPoooyY"))  # True
print(solution("Pyy"))     # False
print(solution("abc"))     # True: 둘 다 없으면 0 == 0
