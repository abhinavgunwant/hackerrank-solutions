#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

char* kth_word_in_mth_sentence_of_nth_paragraph(char**** document, int k, int m, int n) {
    return document[n-1][m-1][k-1];
}

char** kth_sentence_in_mth_paragraph(char**** document, int k, int m) { 
    return  document[m-1][k-1];
}

char*** kth_paragraph(char**** document, int k) {
    return document[k-1];
}

char**** get_document(char* text) {
    int len = strlen(text);
    int paragraph_count = 0;
    int sentence_count = 0;
    int word_count = 0;
    int char_count = 0;
    int i = 0;
    
    for (i=0; i<len; ++i) {
        if (text[i] == '\n') {
            ++paragraph_count;
        }
    }

    ++paragraph_count;

    // printf("\nparagraphs: %d", paragraph_count);

    //// init document with no of paragraphs!

    char **** document = (char ****) malloc((sizeof(char ****)) * paragraph_count);
    char *** paragraph = NULL;
    char ** sentence = NULL;
    char * word = NULL;

    int i_par = 0;
    int i_sentence = 0;
    int i_word = 0;
    int i_char = 0;
    int last_par_pos = 0;
    int next_par_pos = 0;
    int last_sentence_pos = 0;
    int next_sentence_pos = 0;
    int last_word_pos = 0;
    int next_word_pos = 0;

    //// loop over paragraphs
    for (i_par=0; i_par<paragraph_count; ++i_par) {
        sentence_count = 0;

        //// count sentences
        last_par_pos = next_par_pos;

        for (i=last_par_pos; text[i]!='\n' && i<len; ++i) {
            if (text[i] == '.') {
                ++sentence_count;
            }
        }

        next_par_pos = i + 1;

        while (text[next_par_pos] == '\n' || text[next_par_pos] == '.') {
            ++next_par_pos;
        }

        //// allocate space for paragraph based on sentence count
        paragraph = (char ***) malloc((sizeof(char ***)) * sentence_count);

        //// loop over sentences in a paragraph
        for (i_sentence=0; i_sentence<sentence_count; ++i_sentence) {
            word_count = 0;

            //// count words
            last_sentence_pos = next_sentence_pos;
            for (i=last_sentence_pos; text[i]!='.' && i<len; ++i) {
                if (text[i] == ' ') {
                    ++word_count;
                }
            }

            ++word_count;
            next_sentence_pos = i + 1;

            while (text[next_sentence_pos] == '\n' || text[next_sentence_pos] == '.') {
                ++next_sentence_pos;
            }

            //// allocate space for sentence based on word count
            sentence = (char **) malloc((sizeof(char **)) * word_count);

            for (i_word=0; i_word<word_count; ++i_word) {
                char_count = 0;

                last_word_pos = next_word_pos;
                i = last_word_pos;

                while(text[i] != ' ' && text[i] != '.'  && text[i] != '\n'  && i<len) {
                    ++char_count;
                    ++i;
                }

                // ++char_count;
                next_word_pos = i + 1;
                while (text[next_word_pos] == '\n' || text[next_word_pos] == '.' || text[next_word_pos] == ' ') {
                    ++next_word_pos;
                }

                word = (char *) malloc((sizeof(char *)) * (char_count + 1));

                for (i=last_word_pos; i<last_word_pos+char_count; ++i) {
                    word[i - last_word_pos] = text[i];
                }
                word[char_count] = '\0';

                sentence[i_word] = word;
            }

            paragraph[i_sentence] = sentence;
        }

        document[i_par] = paragraph;
    }

    return document;
}


char* get_input_text() {	
    int paragraph_count;
    scanf("%d", &paragraph_count);

    char p[MAX_PARAGRAPHS][MAX_CHARACTERS], doc[MAX_CHARACTERS];
    memset(doc, 0, sizeof(doc));
    getchar();
    for (int i = 0; i < paragraph_count; i++) {
        scanf("%[^\n]%*c", p[i]);
        strcat(doc, p[i]);
        if (i != paragraph_count - 1)
            strcat(doc, "\n");
    }

    char* returnDoc = (char*)malloc((strlen (doc)+1) * (sizeof(char)));
    strcpy(returnDoc, doc);
    return returnDoc;
}

void print_word(char* word) {
    printf("%s", word);
}

void print_sentence(char** sentence) {
    int word_count;
    scanf("%d", &word_count);
    for(int i = 0; i < word_count; i++){
        printf("%s", sentence[i]);
        if( i != word_count - 1)
            printf(" ");
    }
} 

void print_paragraph(char*** paragraph) {
    int sentence_count;
    scanf("%d", &sentence_count);
    for (int i = 0; i < sentence_count; i++) {
        print_sentence(*(paragraph + i));
        printf(".");
    }
}

int main() 
{
    char* text = get_input_text();
    char**** document = get_document(text);

    int q;
    scanf("%d", &q);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 3){
            int k, m, n;
            scanf("%d %d %d", &k, &m, &n);
            char* word = kth_word_in_mth_sentence_of_nth_paragraph(document, k, m, n);
            print_word(word);
        }

        else if (type == 2){
            int k, m;
            scanf("%d %d", &k, &m);
            char** sentence = kth_sentence_in_mth_paragraph(document, k, m);
            print_sentence(sentence);
        }

        else{
            int k;
            scanf("%d", &k);
            char*** paragraph = kth_paragraph(document, k);
            print_paragraph(paragraph);
        }
        printf("\n");
    }     
}