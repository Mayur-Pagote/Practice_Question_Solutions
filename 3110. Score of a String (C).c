#include <stdlib.h> // To use abs() function
#include <string.h> // To use strlen() function

int scoreOfString(char* s) {
  
    int length = strlen(s); // Storing length of string s
    int result = 0; // Initializing result with 0
    int prev, next; // This variables will store ASCII values

    // Looping over s and calculating difference
    for (int i = 0; i<length-1; i++){
        prev = s[i];
        next = s[i+1];
        result += abs(prev - next);
    }
    return result;
}
