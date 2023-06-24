'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
  fly me   to   the moon  '''
# str = "  fly me   to   the moon  "
# lst = list(str.split())
# print(lst)
# print(len(lst[-1]))
class solution:
    def lengthoflastword(self, s: str)-> int:
        lst = list(s.split())
        return len(lst[-1])
s = input()
s1 = solution()
print(s1.lengthoflastword(s))