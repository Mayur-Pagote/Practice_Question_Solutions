int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) {

    int max = 0; // Initializing max variable with 0

    // Iterating through every customer's wealth
    for (int i=0; i<accountsSize; i++){
        int count = 0;
        for (int j=0; j<*accountsColSize; j++){
            count += accounts[i][j];
        }
        if (count>max) max = count;
    }
    return max;
}
