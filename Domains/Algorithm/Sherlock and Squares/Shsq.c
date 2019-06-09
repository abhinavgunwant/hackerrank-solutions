#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int f(int x){
    return x*x;
}

int sq(int num){
    int x = num/4, i, x0;
    for(i=0; i<5; ++i){
        if(f(x) > num){
            x /= 2;
        }else if(f(x) < num){
            x += x/2;
        }else if(f(x) == num){
            return x;
        }
    }

    return x;
}


int main() {
    int t, i, j, a, b, count, num;

    scanf("%d", &t);

    for(i=0; i<t; ++i){
        scanf("%d %d", &a, &b);

        count = 0;
        for(j=a; j<=b; ++j){
            num = sq(j);
            printf(" %d", num);
            if(j == num*num){
                ++count;
            }
        }

        printf("%d", count);

        if(i <t-1){
            printf("\n");
        }
    }

    return 0;
}
