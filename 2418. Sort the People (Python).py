class Solution(object):
    def sortPeople(self, names, heights):
        # Get the length of the names list
        length = len(names)
        
        # Create a dictionary to map heights to names
        name_height_dict = {}
        
        # Initialize an empty list to store the sorted names
        sorted_list = []
        
        # Populate the dictionary with heights as keys and names as values
        for i in range(length):
            name_height_dict[heights[i]] = names[i]
        
        # Sort the heights in descending order
        heights.sort(reverse=True)
        
        # Build the sorted list of names based on the sorted heights
        for i in heights:
            sorted_list.append(name_height_dict[i])
        
        return sorted_list
