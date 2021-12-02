#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define PREAMBLE 25
#define NUM_SET_LENGTH 35

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
    int numbufferSize = 10;
    int* numbuffer = malloc(sizeof(int) * numbufferSize);

    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;

    int invalidNumber = 0;
    int cpos = 0;
    while ((read = getline(&line, &len, stdin)) != -1) {
        if (cpos >= numbufferSize) {
            numbufferSize *= 2;
            numbuffer = realloc(numbuffer, sizeof(int) * numbufferSize);
        }

        int num = atoi(line);
        if (cpos >= PREAMBLE && invalidNumber == 0) {
            if (isSum(ringbuffer, cpos, num) == 0) {
                printf("%d does not follow the rule!\n", num);
                invalidNumber = num;
            }
        }
       
       numbuffer[cpos] = num;
       ringbuffer[cpos++ % PREAMBLE] = num;
    }

    for (int i = 0; i < cpos - NUM_SET_LENGTH; i++) {
        int num = 0;
        int smallestNum = INT32_MAX;
        int largestNum = 0;
        for (int j = 0; j < NUM_SET_LENGTH; j++) {
            if (numbuffer[i + j] < smallestNum)
                smallestNum = numbuffer[i + j];
            if (numbuffer[i + j] > largestNum)
                largestNum = numbuffer[i + j];
            num += numbuffer[i + j];
            if (num > invalidNumber) break;
            else if (num == invalidNumber) {
                printf("from %d through %d produces the invalid number: %d\n", numbuffer[i], numbuffer[i + j], smallestNum + largestNum);
            }
        }
    }

    fclose(stdin);
    if (line) {
        free(line);
    }

    if (numbuffer) {
        free(numbuffer);
    }
    
    return EXIT_SUCCESS; 
}