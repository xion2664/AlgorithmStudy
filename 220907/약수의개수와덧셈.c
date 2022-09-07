#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int left, int right) {
    int answer = 0;
    int count;
    
    for(int n=left ; n<=right ; n++) {
        count=0;
        
        for(int decimal = 1 ; decimal <= n ; decimal++) {
            if(n % decimal == 0)
                count++;
            else
                continue;
        }
        
        if(count%2 == 0)
            answer = answer + n;
        else if(count%2 == 1)
            answer = answer - n;
    }
    
    return answer;
}