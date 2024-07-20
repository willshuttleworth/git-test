#include <stdio.h>

void function(int arg) {
    printf("arg: %d\n", arg);
}

int main(int argc, char** argv) {
    if(argc > 1) {
        printf("hello, %s\n", argv[1]);
    }
    puts("done");
    puts("done 2");
    puts("done 3");
    puts("done 4");
    return 0;
}
