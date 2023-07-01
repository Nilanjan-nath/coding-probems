'''
Given a positive integer N, print count of set bits in it. 

Example 1:

Input:
N = 6
Output:
2
Explanation:
Binary representation is '110' 
So the count of the set bit is 2.
Here i will apply Brian Kernighan's Algorithm.
first we will convert the given number(n) and(n-1) into its binary form and will apply `and` bitwise operator between them.
By doing this, every set bit will be unset(means it will get converted to 0)
We will stop the process when there is no set bits(no 1 bits)that is n will be 0.
The number of steps will be the number of set bits...
MY APPROACH...
'''