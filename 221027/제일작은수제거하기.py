def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        answer = arr
    else:
        answer = [-1]

    return answer
