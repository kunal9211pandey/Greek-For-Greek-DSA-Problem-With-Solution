#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
		result = S[0]
		for i in range(1 ,len(S)):
		    if S[i-1] == ' ':
		        result += S[i]
		return result