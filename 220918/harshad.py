def solution(x):
    answer = True
    sum = 0

    while x > 0:
        sum = sum + (x % 10)
        x = x/10

    if x % sum == 0:
        answer = True
    else:
        answer = False

    return answer
