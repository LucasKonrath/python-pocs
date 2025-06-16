You're given an array of four integers in the range [1, 9], which represent four cards. The objective is to determine whether you can arrange these cards into a mathematical expression that equals 24. This expression should use the standard mathematical operators: addition (+), subtraction (-), multiplication (*), and division (/), as well as parentheses to change the operator precedence if necessary.

The challenge has a few rules:

Division is real division, not integer division, which means you should preserve the fractional part of the result (if any).
You must use the numbers as they are; you cannot use a number as a unary operator (like negation) or concatenate numbers to form new digits.
Each operation must be between two numbers.
Your goal is to return true if such an arrangement is possible that evaluates to 24, otherwise, return false.

## AlgoExpert

679. 24 Game

Hard
Array
Math
Backtracking
Leetcode Link
Problem Description

You're given an array of four integers in the range [1, 9], which represent four cards. The objective is to determine whether you can arrange these cards into a mathematical expression that equals 24. This expression should use the standard mathematical operators: addition (+), subtraction (-), multiplication (*), and division (/), as well as parentheses to change the operator precedence if necessary.

The challenge has a few rules:

Division is real division, not integer division, which means you should preserve the fractional part of the result (if any).
You must use the numbers as they are; you cannot use a number as a unary operator (like negation) or concatenate numbers to form new digits.
Each operation must be between two numbers.
Your goal is to return true if such an arrangement is possible that evaluates to 24, otherwise, return false.

Flowchart Walkthrough

First, let's analyze the problem using the Flowchart. Here's a step-by-step walkthrough:

Is it a graph?

No: The problem does not involve traditional graphs with nodes and edges depicting relationships or connections.
Need to solve for kth smallest/largest?

No: The problem is not about ordering elements or finding a specific element based on its size.
Involves Linked Lists?

No: The problem doesn't use linked lists; it primarily deals with numbers and operations on them.
Does the problem have small constraints?

Yes: The problem has relatively small constraints given there are only four numbers and basic arithmetic operations.
Brute force / Backtracking?

Yes: Brute force or backtracking is suitable as the problem requires exploring various combinations and sequences of operations to achieve the target of 24 from four numbers.
Conclusion: The flowchart suggests using a backtracking approach for trying all possible operations combinations on the given numbers to reach the target value, making the problem suitable for a backtracking pattern.

Intuition

Thinking Process

Given the small size of the problem (four numbers), brute force is a viable strategy. Brute force in this scenario means trying out every possible combination of numbers and operations. Since there are only four numbers and we want to examine every combination of them with every possible operation, we can get all permutations of these numbers and apply different operations between each pair in the permutations.

The problem with typical brute force is that it can sometimes lead to repetitive calculations or it could compute expressions that are not necessarily valid under the given rules. To optimize brute force, we use a recursive function to generate all possible expressions and evaluate them.

Approach

First, we convert the array of integers into a list of doubles so that we can handle real division accurately during the calculations.
We apply a depth-first search (DFS) approach. This means we'll continually dive into one possibility until we reach the end (which is, in this case, one number remaining in our list), evaluate that, and then backtrack to explore other possibilities.
At each step of the recursion, we select two different numbers and perform all possible operations on them. For this, we create a temporary list for each operation—addition, subtraction, multiplication, and both ways of division—as long as the divisor is not zero.
After performing an operation, we add the result back into the list and recursively call the DFS function with this new list which is now one element shorter.
We keep doing this until we're down to a single element in the list. If at any point the single remaining number in the list is equal to 24 (within a small error margin to account for floating-point imprecision), we've found a valid expression and can thus return true.
If none of the combinations result in 24, we return false.
This recursive process allows us to efficiently try out all valid combinations of operations on the given numbers.