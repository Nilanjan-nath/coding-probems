'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].'''
'''My APPROACH
lst = [9,8,7,6,5,4,3,2,1,0]
num =0
for digit in lst:
    num = num*10 + digit
lst =[]
print(num)
num+=1
num = str(num)
for digit in num:
    digit = int(digit)
    lst.append(digit)

print(lst)'''

#BETTER APPROACH
class solution:
    def plus_one(self, digits:list[int])->list:
        return [int(x) for x in str(int(''.join(map(str, digits))) + 1)]    
digits = list(map(int, input().split()))
s = solution()
result_list = s.plus_one(digits)
print(result_list)
