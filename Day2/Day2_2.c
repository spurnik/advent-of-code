/************************************************
 * Advent Of Code Day 2: Dive! part 2
 *
 * @author Arnau Martínez Tomàs
 * @date 02/12/2021
 * 
 ************************************************/ 

#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

    char line[1024];

    FILE* testInput = fopen("./input", "r");
    if (!testInput) {
        printf("Failed to open text file, does the file exist?\n");
        exit(1);
    }
    
    int horizontalValue = 0, depthValue = 0, aimValue = 0;
    int currentValue;
    long multipliedValue;
    int k = 0;

    // Read lines from the input file
    while(fgets(line, sizeof(line), testInput)) {
        if (line[0] == 'f'){
            //printf("Number value: %d\n", atoi(line + 8));
            currentValue = atoi(line + 8);
            horizontalValue += currentValue;
            depthValue += aimValue * currentValue;
        }
        if (line[0] == 'd'){
            //printf("Number value: %d\n", atoi(line + 5));
            aimValue += atoi(line + 5);
        }
        if (line[0] == 'u'){
            //printf("Number value: %d\n", atoi(line + 3));
            aimValue -= atoi(line + 3);
        }
        // Iteration Update
        k++;
    }

    multipliedValue = ((long)horizontalValue * (long)depthValue);

    printf("Number of input lines: %d\n", k);
    printf("Horizontal Final value: %d\n", horizontalValue);
    printf("Depth Final value: %d\n", depthValue);
    printf("Final Multiplication Value: %ld\n", multipliedValue);
    return 0;
}