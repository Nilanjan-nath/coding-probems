'''
Given a number in its binary form find if the given binary number is a multiple of 3. It is recommended to finish the task using one traversal of input binary number.

Example 1:

Input: S = "0011"
Output: 1
Explanation: "0011" is 3, which is divisible by 3.
Hint: In the decimal number system, a number is divisible by 3 if and only if the sum of its digits is divisible by 3. Similarly, in the binary number system, a binary number is divisible by 3 if and only if the difference between the counts of '1's at odd and even positions is divisible by 3.'''
class solution:
    def isdivisible(self, s:str)->int:
        pos=odd=even =0
        for i in s:
            if i=='1':
                if pos%2==0:odd+=1
                else: even+=1
            pos+=1
        return 1 if not abs(odd-even) %3 else 0
s = input()
sol = solution()
result = sol.isdivisible(s)
print(result)