class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Initialize an empty string to hold the defanged IP address
        defangedIP = ""
        
        # Iterate through each character in the input address
        for i in address:
            # If the character is a dot, append "[.]" to defangedIP
            if i == ".":
                defangedIP += "[.]"
            # Otherwise, append the character as it is
            else:
                defangedIP += i

        return defangedIP
