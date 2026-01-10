#User function Template for python3
class Solution:
	def penaltyScore(self, S):
		# code here
		goal = 0
		for i in range(len(S)-1):
		    if S[i] =='2' and S[i + 1] == '1':
		        goal += 1
		return goal