#include <stdio.h>
#include <ctype.h>

int main(){
    int i, n, k, num;
    char s[10240];

    scanf("%d",&n);
    scanf("%s",s);
    scanf("%d",&k);

    for(i=0; i<n; ++i){
        if(isalpha(s[i])){
            num = s[i] + k;
            if((s[i]>='A' && s[i]<='Z')&& num>'Z'){
                num = 'A' + (num - 'A') % 26;
            }
            if((s[i]>='a' && s[i]<='z') && num>'z'){
                num = 'a' + (num - 'a') % 26;
            }
        }else if(isdigit(s[i])){
            num = s[i] + k;
            if(num > '9'){
                num = '0' + (num - '0')%10;
            }
        }else{
            num = s[i];
        }

        printf("%c", num);
    }
    return 0;
}
