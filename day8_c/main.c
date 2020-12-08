#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

volatile int acc;

# define INSTR_NOP 0
# define INSTR_ACC 1
# define INSTR_JMP 2

typedef struct {
    uint8_t instr;
    int imm;
    uint8_t exed;
} instruction;

instruction* loadInstruction(char* line, instruction* instructions) {
    instruction inst;
    inst.instr = INSTR_NOP;
    if (strncmp(line, "acc", 3) == 0) {
        inst.instr = INSTR_ACC;
    } else if (strncmp(line, "jmp", 3) == 0) {
        inst.instr = INSTR_JMP;
    }
    inst.imm = strtol(line+3, NULL, 10);
    inst.exed = 0;

    memcpy(instructions, &inst, sizeof(instruction));

    return instructions + 1;
}

instruction* executeCode(instruction* pos) {
    printf("instr: %d, imm: %d\n", pos->instr, pos->imm);
    pos->exed = 1;
    if (pos->instr == INSTR_JMP) {
        return pos + pos->imm;
    } else if (pos->instr == INSTR_ACC) {
        acc += pos->imm;
    }
    return pos + 1;
}

int main(int argc, char* argv[]) {
    instruction* instructions = calloc(2000, sizeof(instruction));
    instruction* ptr = instructions;

    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;

    while ((read = getline(&line, &len, stdin)) != -1) {
        ptr = loadInstruction(line, ptr);
    }

    fclose(stdin);
    if (line) {
        free(line);
    }

    acc = 0;
    ptr = instructions;
    for (int i = 0; i < 1000; i++) {
        if (ptr->exed == 1) {
            printf("Loop detected at acc: %d\n", acc);
            break;
        }
        ptr = executeCode(ptr);
    }

    if (instructions) {
        free(instructions);
    }
    
    return EXIT_SUCCESS; 
}