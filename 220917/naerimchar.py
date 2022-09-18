def solution(n):
    answer = 0

#     j_list = []

#     while n>0 :
#         j_list.append(n%10)
#         n = n/10

#     j_list.sort(reverse=True)

#     for j in j_list :
#         answer = answer + j

    ls = list(str(int(n)))
    ls.sort(reverse=True)
    answer = int("".join(ls))

    return answer
