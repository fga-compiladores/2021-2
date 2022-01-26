
#include<stdio.h>

void main() {
    char array[30000] = {0};
    char *ptr = array;
    while (*ptr) {
    --*ptr;
    ++ptr;
    ++*ptr;
    --ptr;
    }
}

