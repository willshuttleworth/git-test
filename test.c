#include <stdio.h>

int main(int argc, char** argv) {
    if(argc > 0) {
        printf("hello, %s\n", argv[1]);
    }
    return 0;
}
