#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(){
    int t, n, a0, count, num, i, dig;
    char str[1024];
    scanf("%d",&t);
    for(a0 = 0; a0 < t; a0++){
        count = 0;
        scanf("%d", &num);
        n = num;
        while(n){
            dig = n%10;
            n /= 10;
            if(dig){
                if(num%dig == 0){
                    ++count;
                }
            }
        }

        printf("%d", count);

        if(a0 < t-1){
            printf("\n");
        }
    }
    return 0;
}
