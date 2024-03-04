# phase-3-week-1-python-toy-problem-code-challenge

## Challenge 1:

### Function Description

The function solution(A) takes in a list A representing the number of bricks in each box and calculates the minimum number of moves required to equalize the number of bricks in each box. It returns the minimum number of moves or -1 if it's not possible to equalize the number of bricks.

### Input

A: A list of integers representing the number of bricks in each box.

### Output

Returns the minimum number of moves required to equalize the number of bricks in each box, or -1 if it's not possible.

### Approach

1. Initialize variables moves, total_moves, N, and available_bricks.
2. Calculate the total number of available bricks.
3. Calculate the total number of required bricks.
4. If the available bricks are not equal to the required bricks, return -1 as it's not possible to equalize the number of bricks.
5. Otherwise, calculate the average number of bricks per box.
6. Iterate through each box and calculate the difference between the average number of bricks and the number of bricks in each box.
7. Add the absolute difference to moves.
8. Return the minimum number of moves.

## Challenge 2:

### Function description

The function solution(A) calculates the maximum sum of two numbers in a given list A such that they have the same digit sum. The function utilizes a dictionary to keep track of the maximum sum for each unique digit sum encountered.

### Input

A: A list of integers representing numbers.

### Output

max_sum: An integer representing the maximum sum of two numbers with the same digit sum.

### Approach

1. Initialize an empty dictionary digit_sums to store the digit sum as keys and the corresponding number as values.
2. Initialize a variable max_sum to -1 to keep track of the maximum sum of numbers with the same digit sum.
3. Iterate through each number num in the input list A.
4. Calculate the digit sum of the current number num by converting it to a string, then summing its digits after converting them back to integers.
5. Check if the current digit sum exists in the digit_sums dictionary.

- If it exists:
  - Update max_sum with the maximum of its current value and the sum of the current number num and the corresponding number in the dictionary digit_sums.
- If it doesn't exist:
  - Add the current digit sum to the digit_sums dictionary with the current number num.

6. Return the max_sum after iterating through all numbers in the input list A.

## Challenge 3:

### Function Description:

The function, solution(N), generates a string consisting of lowercase English alphabets repeated based on the input integer N. The function uses modular arithmetic to handle cases where N exceeds the length of the alphabet.

### Input:

N: An integer representing the desired length of the output string.

### Output:

result: A string containing lowercase English alphabets repeated based on the input N.

### Algorithm:

1. Define the lowercase English alphabet as a string alphabet.
2. Initialize an empty string result to store the final output.
3. Calculate the number of full cycles of the alphabet that can fit into N by dividing N by the length of the alphabet (26) and storing the result in full_cycles.
4. Append alphabet repeated full_cycles times to result.
5. Calculate the remainder of N divided by 26 and store it in remainder.
6. Append the first remainder characters of alphabet to result.
7. Return the final string result.
