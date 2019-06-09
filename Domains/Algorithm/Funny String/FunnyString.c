#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void reverse(char *a, char *temp);

int main() {
    int i, j, t, arr[10], len, k;
    char str[10000], rev[10000];

    scanf("%d", &t);

    for(i=0; i<t; ++i){
        k = 1;
        scanf("%s", str);
        len = strlen(str);
        reverse(str, rev);
        //printf("%s\n", rev);
        for(j=1; j<len; ++j){
            if(abs(str[j]-str[j-1]) != abs(rev[j]-rev[j-1])){
                //printf("\nj=%d %d %d\t", j, (int)abs(str[j]-str[j-1]), (int)abs(rev[j]-rev[j-1]));
                k=0;
                break;
            }
            /*
            if(((int)fabs(str[j]-str[j-1])) != ((int)fabs(str[len-j]-str[len-j+1]))){
                printf("\nj=%d %d %d\t", j, (int)fabs(str[j]-str[j-1]), (int)fabs(str[len-j]-str[len-j+1]));
                k=0;
                break;
            }
            */
        }

        if(k){
            arr[i] = 1;
        }else{
            arr[i] = 0;
        }
    }

    for(i=0; i<t; ++i){
        if(arr[i]){
            printf("Funny");
        }else{
            printf("Not Funny");
        }

        if(i < t-1){
            printf("\n");
        }
    }
    return 0;
}

void reverse(char *a, char *temp){
    int l = strlen(a), i, j;
    for(i=l-1, j=0; i>=0; --i, ++j){
        temp[j] = a[i];
    }
    temp[++j] = '\0';
}
