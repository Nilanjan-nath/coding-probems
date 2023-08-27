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
class solution:
    def convert_to_bin(self, n:int)->str:
        bin_str = ""
        while(n!=0):
            rem = n%2
            bin_str = str(rem)+bin_str
            n = n//2
            if n==0:
                bin_str = '0'+bin_str
        if len(bin_str)<3:
            bin_str = '0'+bin_str
        return bin_str
    def convert_to_decimal(self, result:str)->int:
        sum =0
        p = len(result)-1
        for i in result:
            i = int(i)
            sum = sum+ i * 2**p
        return sum
    def setBits(self, N):
        count =0
       
        while(N!=0):
            n_bits = self.convert_to_bin(N)
            n_minusone_bits = self.convert_to_bin((N-1))
            result = ''.join(map(lambda x, y: str(int(x) and int(y)), n_bits, n_minusone_bits))
            print(result)
            N = self.convert_to_decimal(result)
            print(N)
            
            count+=1
        return count
n = 11
s = solution()
count_set_bits = s.convert_to_bin(n)
print(count_set_bits)

	
    