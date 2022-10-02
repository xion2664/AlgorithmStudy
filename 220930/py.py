def solution(s):
    answer = True

    p = 0
    y = 0

    for i in s:
        if(i == "P" or i == "p"):
            p = p+1
        elif(i == "Y" or i == "y"):
            y = y+1

    if p != y:
        answer = False

    return answer
