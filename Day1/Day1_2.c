/************************************************
 * Advent Of Code Day 1: Sonar Sweep part 2
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
    
    int largerWindowCounter = 0;

    int window[3] = {0,0,0}; // A, B, C
    int currentValue, currentWindowValue, previousWindowValue;

    int k = 0;

    // Read lines from the input file
    while(fgets(line, sizeof(line), testInput)) {
        currentValue = atoi(line);

        // Reset windows based on k's modulo 3
        window[k % 3] = 0;

        window[0] += currentValue;
        window[1] += currentValue;
        window[2] += currentValue;

        // Current Window Valuen (the next who will be erased)
        currentWindowValue = window[(k + 1) % 3];

        // First three measurements don't count (no previousValue to compare)
        if (k > 2){
            if (previousWindowValue < currentWindowValue)
                largerWindowCounter++;

        } 
        
        //printf("Line %d, Window (%d,%d,%d), ", k, window[0], window[1], window[2]);
        //printf("Current %d, Previous %d\n", currentWindowValue, previousWindowValue);
        
        // Iteration Update
        previousWindowValue = currentWindowValue;
        k++;

    }

    printf("Number of input lines: %d\n", k);
    printf("Counted larger values: %d\n", largerWindowCounter);

    return 0;
}