#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const char* a, const char* b) {
    int i;

    int a_len = strlen(a);
    int b_len = strlen(b);

    int min_len = a_len;

    if(min_len > b_len){
        min_len = b_len;
    }

    for(i=0; i<min_len; ++i){
        if(a[i] < b[i]){
            return -1;
        }

        if(a[i] > b[i]){
            return 1;
        }
    }

    return 0;
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return lexicographic_sort(a, b) * -1;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int i;
    int j;

    int a_length = strlen(a);
    int b_length = strlen(b);

    int found;

    char * a_dict = malloc(sizeof(char) * 1);
    char * b_dict = malloc(sizeof(char) * 1);
    char * temp;

    strcpy(a_dict, "");
    strcpy(b_dict, "");

    char s[2] = "\0";

    //// find the unique characters in a
    for(i=0; i<a_length; ++i){
        found = 0;

        for(j=0; j<strlen(a_dict); ++j){
            if(a_dict[j] == a[i]){
                found = 1;
                break;
            }
        }

        if(found){
            temp = malloc(sizeof(char) * strlen(a_dict));
            strcpy(temp, a_dict);

            s[0] = a[i];

            free(a_dict);
            a_dict = malloc((strlen(temp)+1) * sizeof(char));
            strcpy(a_dict, temp);
            strcat(a_dict, s);

            free(temp);
        }
    }

    //// find the unique characters in b
    for(i=0; i<b_length; ++i){
        found = 0;

        for(j=0; j<strlen(b_dict); ++j){
            if(b_dict[j] == b[i]){
                found = 1;
                break;
            }
        }

        if(found){
            temp = malloc(sizeof(char) * strlen(b_dict));
            strcpy(temp, b_dict);

            free(b_dict);
            b_dict = malloc((strlen(temp)+1) * sizeof(char));

            s[0] = a[i];

            strcpy(b_dict, temp);
            strcat(b_dict, s);

            free(temp);
        }
    }

    if(strlen(a_dict) < strlen(b_dict)){
        return -1;
    }

    if(strlen(a_dict) > strlen(b_dict)){
        return 1;
    }

    return 0;
}

int sort_by_length(const char* a, const char* b) {
    int i;
    int a_length = strlen(a);
    int b_length = strlen(b);

    if(a_length < b_length){
        return -1;
    }

    if(a_length > b_length){
        return 1;
    }

    return 0;
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    int i;
    int j;

    int comp_result;

    int temp_len = -1;

    char * temp;

    for(i=0; i<len; ++i){
        for(j=0; j<len-1; ++j){
            comp_result = cmp_func(arr[i][j], arr[i][j+1]);
            temp_len = strlen(arr[i][j]);

            if (temp_len < strlen(arr[i][j+1])){
                temp_len = strlen(arr[i][j+1]);
            }

            if(comp_result == 1){
                temp = malloc(temp_len * sizeof(char));

                strcpy(temp, arr[i][j+1]);
                strcpy(arr[i][j+1], arr[i][j]);
                strcpy(arr[i][j], temp);

                free(temp);
            }
        }
    }


}


int main()
{
    int n;
    scanf("%d", &n);

    char** arr;
        arr = (char**)malloc(n * sizeof(char*));

    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }

    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");
}
