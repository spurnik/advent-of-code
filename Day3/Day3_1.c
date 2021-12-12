
/************************************************
 * Advent Of Code Day 3: Binary Diagnostic
 *
 * @author Arnau Martínez Tomàs
 * @date 03/12/2021
 * 
 ************************************************/ 

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

#define LINE_LENGHT 13  // Including the newline character
#define MAX_NUMBER_OF_LINES 1000

int main(int argc, char *argv[]) {
 
    // File of data input
    FILE* testInput = fopen("./input", "r");
    if (!testInput) {
        printf("Failed to open text file, does the file exist?\n");
        exit(1);
    }

    // File Descriptor
    int fd = fileno(testInput);

    // Get the length of the file (could be done with fseek)
    struct stat buf;
    fstat(fd, &buf);
    
    // mmap of the file as the data
    char *data = (char *) mmap(NULL, buf.st_size, PROT_READ, MAP_SHARED, fd, 0);
    if(data == MAP_FAILED) {
        printf("Error allocating matrix. Aborting\n");
        exit(1);
    }

    // Value counters (0's, 1's) for each column
    int countZeros[LINE_LENGHT], countOnes[LINE_LENGHT];

    for (int i = 0; i < LINE_LENGHT; i++){
        countZeros[i] = 0; 
        countOnes[i] = 0;
    }

    for (int k; k < (int) buf.st_size; k++){
        if (data[k] == '0') countZeros[k % LINE_LENGHT]++;
        if (data[k] == '1') countOnes[k % LINE_LENGHT]++;
    }

    int gamma = 0, epsilon = 0;
    char value;
    for (int i = LINE_LENGHT - 2; i >= 0; i--){
        printf("Ones: %d, Zeros: %d\n", countOnes[i], countZeros[i]);
        if (countOnes[i] >= countZeros[i]) value = 1;
        else value = 0;
        gamma += value * pow(2, ((LINE_LENGHT - 2) - i));
        epsilon += (1 - value) * pow(2, ((LINE_LENGHT - 2) - i));
    }

    printf("Gamma: %d\n", gamma);
    printf("Epsilon: %d\n", epsilon);
    printf("Result Part 1: %d\n", gamma * epsilon);

    // Free the memory mapped
    munmap(data, buf.st_size);

    return 0;
}


/*  Another possible implementation for mapping the file lines (without knowing it's full length)

    // Data Columns of the lines
    char* data[LINE_LENGHT];

    // Allocate enought memory for each line of the file
    for(int j = 0; j < LINE_LENGHT; j++)
        data[j] = (char*) malloc(MAX_NUMBER_OF_LINES * sizeof(char));
    
    // Iterate over the lines of the file, 
    // mapping the columns of the lines onto the data matrix
    char line[1024];
    int counter = 0;
    while(fgets(line, sizeof(line), testInput)){
        
        if (counter == MAX_NUMBER_OF_LINES){
            printf("Error, max number of allocated space reached.");
            exit(1);
        }

        // data[0] (first column) to data[LINE_LENGHT - 1] (last column)
        for (int j = 0; j < LINE_LENGHT; j++)
            data[j][counter] = line[j];

        counter++;
    }

    if (counter < MAX_NUMBER_OF_LINES)
        for(int j = 0; j < LINE_LENGHT; j++)
            data[j] = (char*) realloc(data[j], counter * sizeof(char));

    for(int j = 0; j < LINE_LENGHT; j++)
        free(data[j]);

    */