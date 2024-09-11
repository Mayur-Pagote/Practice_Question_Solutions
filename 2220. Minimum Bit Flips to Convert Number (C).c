int minBitFlips(int start, int goal) {
    int count = 0; // Initialize the count of bit flips required

    // Continue processing until both start and goal are reduced to 0
    while (start || goal) {

      // Check if the least significant bit of start differs from the least significant bit of goal
      if ((start & 1) != (goal & 1)) {
          count += 1; // Increment count if bits are different
      }

      // Right shift both start and goal by 1 bit (essentially dividing by 2)
      start = start / 2; // Move to the next bit by dividing by 2
      goal = goal / 2;   // Move to the next bit by dividing by 2
    }

    return count; // Return the total count of bit flips needed
}
