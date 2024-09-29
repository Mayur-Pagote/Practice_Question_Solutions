#include <vector>
using namespace std;

class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        // Convert Celsius to Kelvin
        double kelvin = celsius + 273.15;
        
        // Convert Celsius to Fahrenheit
        double fahrenheit = celsius * 1.80 + 32.00;

        // Create a vector to store the converted temperatures
        vector<double> arr;
        
        // Add Kelvin temperature to the vector
        arr.push_back(kelvin);
        
        // Add Fahrenheit temperature to the vector
        arr.push_back(fahrenheit);

        // Return the vector containing both temperatures
        return arr;   
    }
};
