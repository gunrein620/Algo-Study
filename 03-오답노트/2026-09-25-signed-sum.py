# 음양 더하기
# 내 실수: 중첩 for로 모든 조합을 만들었다. 같은 위치끼리는 zip.
# True는 양수, False는 음수. append[-num]이 아니라 append(-num).


def solution(absolutes, signs):
    answer = []
    for num, sign in zip(absolutes, signs):
        if sign:
            answer.append(num)
        else:
            answer.append(-num)
    return sum(answer)


# 짧게: sum(num if sign else -num for num, sign in zip(absolutes, signs))
print(solution([4, 7, 12], [True, False, True]))  # 9
