class Solution {
public:
    string defangIPaddr(string address) {
        // Initialize an empty string to hold the defanged IP address
        string defangedIP;
        
        // Get the length of the input address
        int length = address.size();
        
        // Iterate through each character in the input address
        for (int i = 0; i < length; i++) {
            // If the character is a dot, append "[.]" to defangedIP
            if (address[i] == '.') 
                defangedIP += "[.]";
            // Otherwise, append the character as it is
            else 
                defangedIP += address[i];
        }
        
        return defangedIP;
    }
};
