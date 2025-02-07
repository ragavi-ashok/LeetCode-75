"""
Question 1- Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

"""

"""
Approach for Solving "Merge Strings Alternately"

Step 1: Clarifying the Problem Statement

Before jumping into coding, it's essential to clarify the problem to ensure understanding. 

Questions to ask the interviewer:

    1.Input Constraints

What are the minimum and maximum lengths of word1 and word2?

Do they only contain lowercase English letters?

    2.Expected Output

Should the merged string maintain the original order of characters?

What should happen if one string is longer than the other?

    3.Edge Cases

What if word1 is empty? What if word2 is empty?

What if both strings are of equal length?

What if one string is significantly longer than the other?



Step 2: Understanding the Requirements

Based on the problem statement and constraints:

We need to merge the strings by alternating characters from word1 and word2.

If one string is longer, append the remaining characters to the merged result.

We can assume word1 and word2 have at least one character.



Step 3: Thinking About an Efficient Approach

Approach: Iterative Merge Using a List

Use a pointer i to iterate through both strings.

Append characters from word1 and word2 alternately to a list.

If one string is exhausted, append the remainder of the other string.

Convert the list back to a string and return the result.

Time Complexity Analysis:

We iterate through both strings at most once, leading to O(n + m) time complexity, where n and m are the lengths of word1 and word2.

Space complexity is O(n + m) for storing the result.



Step 4: Writing the Code and Explaining Line by Line

Below is an implementation using the iterative approach:
    
"""

word1 = input("Enter the word1:")
word2 = input("Enter the word2:")
class Solution():
    def mergeAlternately(self, word1, word2) -> str:
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []  # Initialize an empty list to store merged characters
        i = 0  # Initialize index variable
        
        # Loop runs until all characters in both words are processed
        while i < len(word1) or i < len(word2):
            if i < len(word1):  # If word1 still has characters left, append the next character
                result.append(word1[i])
            if i < len(word2):  # If word2 still has characters left, append the next character
                result.append(word2[i])
            i += 1  # Move to the next index
        
        return ''.join(result)  # Convert the list into a string and return
    
sol = Solution()
print(sol.mergeAlternately(word1, word2))


""" 
How to Explain as You Code

Start with the initialization: "We begin by initializing an empty list result to store the merged characters and a counter i to track the index."

Describe the while loop: "This loop continues until both word1 and word2 have been fully processed."

Explain the conditions: "If i is within the bounds of word1, we append the character at i. The same logic applies to word2."

Incrementing the index: "After processing a character from both words, we increment i to move forward."

Final step: "Finally, we convert the list into a string using join() and return the result."

Step 5: Testing

Let's take the example where word1 = "abc" and word2 = "pqr":

Initialization:
result = []
i = 0
First iteration (i = 0):
i < len(word1) is true (0 < 3), so append 'a' to result.
i < len(word2) is true (0 < 3), so append 'p' to result.
result = ['a', 'p']
Increment i to 1.
Second iteration (i = 1):
i < len(word1) is true (1 < 3), so append 'b' to result.
i < len(word2) is true (1 < 3), so append 'q' to result.
result = ['a', 'p', 'b', 'q']
Increment i to 2.
Third iteration (i = 2):
i < len(word1) is true (2 < 3), so append 'c' to result.
i < len(word2) is true (2 < 3), so append 'r' to result.
result = ['a', 'p', 'b', 'q', 'c', 'r']
Increment i to 3.
Fourth iteration (i = 3):
i < len(word1) is false (3 < 3 is false).
i < len(word2) is false (3 < 3 is false).
The loop ends.
Final step:
Join result into a single string: 'apbqcr'


Let’s take an example where word1 = "ab" (length 2) and word2 = "pqrs" (length 4):

Step-by-Step Execution:

Initialization:
result = []
i = 0
First iteration (i = 0):
i < len(word1) is true (0 < 2), so append 'a' to result.
i < len(word2) is true (0 < 4), so append 'p' to result.
result = ['a', 'p']
Increment i to 1.
Second iteration (i = 1):
i < len(word1) is true (1 < 2), so append 'b' to result.
i < len(word2) is true (1 < 4), so append 'q' to result.
result = ['a', 'p', 'b', 'q']
Increment i to 2.
Third iteration (i = 2):
i < len(word1) is false (2 < 2 is false), so skip appending from word1.
i < len(word2) is true (2 < 4), so append 'r' to result.
result = ['a', 'p', 'b', 'q', 'r']
Increment i to 3.
Fourth iteration (i = 3):
i < len(word1) is false (3 < 2 is false), so skip appending from word1.
i < len(word2) is true (3 < 4), so append 's' to result.
result = ['a', 'p', 'b', 'q', 'r', 's']
Increment i to 4.
Fifth iteration (i = 4):
i < len(word1) is false (4 < 2 is false).
i < len(word2) is false (4 < 4 is false).
The loop ends.
Final step:
Join result into a single string: 'apbqrs'

"""







