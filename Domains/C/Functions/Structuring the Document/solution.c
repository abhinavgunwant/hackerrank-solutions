#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

struct word {
    char* data;
};

struct sentence {
    struct word* data;
    int word_count;//denotes number of words in a sentence
};

struct paragraph {
    struct sentence* data  ;
    int sentence_count;//denotes number of sentences in a paragraph
};

struct document {
    struct paragraph* data;
    int paragraph_count;//denotes number of paragraphs in a document
};

struct document get_document(char* text) {
    int len = strlen(text);
    int paragraph_count = 0;
    int sentence_count = 0;
    int word_count = 0;
    int char_count = 0;
    int i = 0;
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
    
    for (i=0; i<len; ++i) {
        if (text[i] == '\n') {
            ++paragraph_count;
        }
    }

    ++paragraph_count;

    //// init document with no of paragraphs!
    struct document doc;
    struct paragraph * paragraph_;
    struct sentence * sentence_;
    struct word * word_;
    char * wordData;

    paragraph_ = (struct paragraph*) malloc((sizeof(struct paragraph)) * paragraph_count);

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
        sentence_ = (struct sentence*) malloc((sizeof(struct sentence)) * sentence_count);

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
            word_ = (struct word*) malloc((sizeof(struct word)) * word_count);

            for (i_word=0; i_word<word_count; ++i_word) {
                char_count = 0;

                last_word_pos = next_word_pos;
                i = last_word_pos;

                while(text[i] != ' ' && text[i] != '.'  && text[i] != '\n'  && i<len) {
                    ++char_count;
                    ++i;
                }

                next_word_pos = i + 1;
                while (text[next_word_pos] == '\n' || text[next_word_pos] == '.' || text[next_word_pos] == ' ') {
                    ++next_word_pos;
                }

                wordData = (char *) malloc((sizeof(char *)) * (char_count + 1));

                for (i=last_word_pos; i<last_word_pos+char_count; ++i) {
                    wordData[i - last_word_pos] = text[i];
                }
                wordData[char_count] = '\0';
                word_[i_word].data = wordData;
            }
            sentence_[i_sentence].data = word_;
            sentence_[i_sentence].word_count = word_count;
        }
        paragraph_[i_par].data = sentence_;
        paragraph_[i_par].sentence_count = sentence_count;
    }

    doc.data = paragraph_;
    doc.paragraph_count = paragraph_count;

    return doc;
}

struct word kth_word_in_mth_sentence_of_nth_paragraph(struct document Doc, int k, int m, int n) {
    return Doc.data[n-1].data[m-1].data[k-1];
}

struct sentence kth_sentence_in_mth_paragraph(struct document Doc, int k, int m) {
    return Doc.data[m-1].data[k-1];
}

struct paragraph kth_paragraph(struct document Doc, int k) {
    return Doc.data[k-1];
}

void print_word(struct word w) {
    printf("%s", w.data);
}

void print_sentence(struct sentence sen) {
    for(int i = 0; i < sen.word_count; i++) {
        print_word(sen.data[i]);
        if (i != sen.word_count - 1) {
            printf(" ");
        }
    }
}

void print_paragraph(struct paragraph para) {
    for(int i = 0; i < para.sentence_count; i++){
        print_sentence(para.data[i]);
        printf(".");
    }
}

void print_document(struct document doc) {
    for(int i = 0; i < doc.paragraph_count; i++) {
        print_paragraph(doc.data[i]);
        if (i != doc.paragraph_count - 1)
            printf("\n");
    }
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

int main() 
{
    char* text = get_input_text();
    struct document Doc = get_document(text);

    int q;
    scanf("%d", &q);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 3){
            int k, m, n;
            scanf("%d %d %d", &k, &m, &n);
            struct word w = kth_word_in_mth_sentence_of_nth_paragraph(Doc, k, m, n);
            print_word(w);
        }

        else if (type == 2) {
            int k, m;
            scanf("%d %d", &k, &m);
            struct sentence sen= kth_sentence_in_mth_paragraph(Doc, k, m);
            print_sentence(sen);
        }

        else{
            int k;
            scanf("%d", &k);
            struct paragraph para = kth_paragraph(Doc, k);
            print_paragraph(para);
        }
        printf("\n");
    }     
}