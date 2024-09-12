class Solution {
public:
    // Return the digital root of num using the formula 1 + (num - 1) % 9
    int addDigits(int num) {
        if (num == 0) return 0;
        return 1 + (num - 1) % 9;
    }
};
