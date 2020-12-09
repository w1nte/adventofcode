#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define PREAMBLE 25

uint8_t isSum(int* ringbuffer, int cpos, int num) {

    for (int i = 0; i < PREAMBLE; i++) {
        for (int j = i; j < PREAMBLE; j++) {
            int num1 = ringbuffer[(cpos - i) % PREAMBLE];
            int num2 = ringbuffer[(cpos - j) % PREAMBLE];
            if (num1 + num2 == num) {
                return 1;
            }
        }
    }

    return 0;
}

int main(int argc, char* argv[]) {
    int ringbuffer[PREAMBLE];

    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;

    int i = 0;
    while ((read = getline(&line, &len, stdin)) != -1) {
        int num = atoi(line);
        if (i >= PREAMBLE) {
            if (isSum(ringbuffer, i, num) == 0) {
                printf("%d does not follow the rule!\n", num);
                break;
            }
        }
       
       ringbuffer[i++ % PREAMBLE] = num;
    }

    fclose(stdin);
    if (line) {
        free(line);
    }
    
    return EXIT_SUCCESS; 
}