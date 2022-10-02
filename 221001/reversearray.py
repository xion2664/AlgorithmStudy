def solution(n):
    answer = []

    arr = list(str(n))
    arr.reverse()

    answer = list(map(int, arr))

    return answer
