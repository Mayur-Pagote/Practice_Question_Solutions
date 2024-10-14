class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Initialize an empty list to store the results
        fblist = []
        
        # Iterate through numbers from 1 to n (inclusive)
        for i in range(1, n + 1):
            # Check if the number is divisible by both 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                fblist.append("FizzBuzz")  # Append "FizzBuzz" if true
            # Check if the number is divisible by 3
            elif i % 3 == 0:
                fblist.append("Fizz")  # Append "Fizz" if true
            # Check if the number is divisible by 5
            elif i % 5 == 0:
                fblist.append("Buzz")  # Append "Buzz" if true
            else:
                fblist.append(str(i))  # Append the number itself if none of the above are true

        return fblist 
