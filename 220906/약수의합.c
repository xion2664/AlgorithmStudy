#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n)
{
    int answer = 0;
    int d;

    for (d = 1; d <= n; d++)
    {
        if (n % d == 0)
            answer = answer + d;
        else
            continue;
    }

    return answer;
}