# 시저 암호
# 막힌 점: 문자 코드로 이동하는 아이디어는 맞았지만, 끝에서 순환하는 법을 몰랐다.
# 핵심: (현재 위치 + 이동량) % 전체 개수. 위치는 0부터 시작한다.
# chr는 자동으로 순환하지 않는다: chr(ord('z') + 1)은 '{'.


def solution(s, n):
    answer = []
    for ch in s:
        if ch == ' ':
            answer.append(ch)
            continue

        base = ord('A') if ch.isupper() else ord('a')
        idx = ord(ch) - base       # 문자 코드를 알파벳 위치 0~25로 바꾼다.
        moved = (idx + n) % 26     # 26은 0으로, 27은 1로 돌아온다.
        answer.append(chr(base + moved))  # 위치를 문자 코드로 되돌린 뒤 문자로.

    return ''.join(answer)


# 'z'를 2칸 이동: 122 - 97 = 25 → (25 + 2) % 26 = 1 → chr(97 + 1) = 'b'
print(solution('z', 2))      # b
print(solution('AB', 1))     # BC
print(solution('a B z', 4))  # e F d
