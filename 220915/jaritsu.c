#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n)
{
    int answer = 0;
    int i, j;

    while (n > 0)
    {
        answer = answer + (n % 10);
        n = n / 10;
    }
    return answer;
}