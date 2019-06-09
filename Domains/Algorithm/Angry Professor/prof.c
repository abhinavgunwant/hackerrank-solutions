//Problem: Angry Professor
//Result: Accepted

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

char res[10][4];

void calc(int curr_t, int n, int k, int *a){
    int stu_count = 0;
	int i;
    for(i=0; i<k; ++i){
        if(a[i] <= 0){
            ++stu_count;
        }
    }
    
    if(stu_count >= k){
        strcpy(res[curr_t], "NO");
        return;
    }
    
    strcpy(res[curr_t], "YES");
}

int main(){
	int t, n, k; 
	int a0, i;
	scanf("%d",&t);

    for(a0 = 0; a0 < t; a0++){
        scanf("%d %d",&n,&k);
        int a[n];
		int a_i;
        for(a_i = 0; a_i < n; a_i++){
           scanf("%d",&a[a_i]);
        }
        
        calc(a0, n, k, a);
    }
    
    for(i=0; i<t; ++i){
        printf("%s", res[i]);
		if(i<t-1){
			printf("\n");
		}
    }
    return 0;
}

