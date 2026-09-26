# 3진법 뒤집기 — 진법 변환 두 방향
# 몰랐던 것: 나머지·몫으로 진법을 바꾸는 방법, int(문자열, 진법).
# 아래에서는 입력 숫자를 n, 진법을 base라고 부른다.


# 1. 10진수 → base진법: 나머지를 모으고, 몫을 다시 나눈다.
# 나머지는 끝자리부터 나오므로 보통은 마지막에 뒤집어야 한다.
# 45 ÷ 3 → 몫 15, 나머지 0
# 15 ÷ 3 → 몫  5, 나머지 0
#  5 ÷ 3 → 몫  1, 나머지 2
#  1 ÷ 3 → 몫  0, 나머지 1
# 나온 순서 "0021" → 뒤집으면 원래 3진법 "1200"
def to_base(n, base):  # 0 이상의 정수, base는 2~36
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result += digits[n % base]
        n //= base
    return result[::-1]


print(to_base(45, 3))  # 1200
print(to_base(10, 2))  # 1010

# 2. base진법 문자열 → 정수: int(문자열, base)
# 오른쪽부터 자리 값이 1, base, base², ...로 커진다.
# 3진수 "0021" = 0×27 + 0×9 + 2×3 + 1×1 = 7
print(int('0021', 3))  # 7
print(int('1200', 3))  # 45
print(int('1010', 2))  # 10
# int('0021')은 기본 10진법이므로 21. 두 번째 인자가 해석할 진법이다.


# 이 문제: 나머지를 모은 순서가 이미 뒤집힌 3진법 → 다시 뒤집지 않는다.
def solution(n):
    reversed_digits = ''
    while n > 0:
        reversed_digits += str(n % 3)
        n //= 3
    return int(reversed_digits, 3)


print(solution(45))   # 7
print(solution(125))  # 229
