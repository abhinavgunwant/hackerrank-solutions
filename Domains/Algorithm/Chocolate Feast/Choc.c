#include <stdio.h>
#include <stdlib.h>

int main(){
    int i, t, n, c, m, k, k_, p, n0;
    scanf("%d", &t);
    for(i=0; i<t; i++){
        scanf("%d %d %d", &n0, &c, &m);
        k = n0/c;
        n = k;
        p = k_ = 0;
        //while(n>0 && p<n0)
        do{
            //printf("\nk_ = %d, n = %d", k_, n);
            k_ = n/m;
            n = n % m;
            k += k_;
            n += k_;
            /*
            k += n/c;
            k_ = k%c;
            n -= k*c;
            k += (k+k_)/m;
            */
            //++p;
        }while(k_ != 0);

        //printf("");
        printf("%d", k);

        if(i < t-1){
            printf("\n");
        }
    }
    return 0;
}
