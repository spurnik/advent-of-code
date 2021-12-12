/************************************************
 * Advent Of Code Day 1: Sonar Sweep
 *
 * @author Arnau Martínez Tomàs
 * @date 01/12/2021
 * 
 ************************************************/ 

#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

    char line[1024];

    FILE* testInput = fopen("./input.txt", "r");
    if (!testInput) {
        printf("Failed to open text file, does the file exist?\n");
        exit(1);
    }
    
    int largerCounter = 0;
    int currentValue, previousValue;

    int k = 0;

    // Read lines from the input file
    while(fgets(line, sizeof(line), testInput)) {
        currentValue = atoi(line);

        // First measurement doesn't count
        if (k != 0){

            if (previousValue < currentValue)
                largerCounter++;
        } 
        
        // Iteration Update
        previousValue = currentValue;
        k++;
    }

    printf("Number of input lines: %d\n", k);
    printf("Counted larger values: %d\n", largerCounter);

    return 0;
}