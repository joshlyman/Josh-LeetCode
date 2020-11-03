# A greedy solution using three sliding windows where you keep track of the best indexes/sums as you go.

# O(n) time: Since we're only going through the list once and using no complex operations, this is O(n).
# O(1) space: Just a fixed set of temp vars. We don't need the extra arrays that the DP solutions have.

# sliding window using 3 pointers
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestTwoSeq = [0, k]
        bestThreeSeq = [0, k, k*2]

        # Sums of each window
        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k*2])
        seqThreeSum = sum(nums[k*2:k*3])

        # Sums of combined best windows
        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        # Current window positions
        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k*2 + 1
        while threeSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]
            
            # Update best single window
            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            # Update best two windows
            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            # Update best three windows
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1

        return bestThreeSeq

# Time: O(N)
# Space:O(1)


# Other solution
# three windows size==k:w1,w2,w3,can just keep 3 adjacent windows move.
# just like dp,since 3 is small, we can do it manually, update maxw1 if w1>maxw1=> update maxw2 if maxw1+w2>maxw2=>update maxw3 if maxw2+w3>maxw3

class Solution(object):
    def maxSumOfThreeSubarrays(self,nums, k):
        w1,w2,w3=sum(nums[:k]),sum(nums[k:2*k]),sum(nums[2*k:3*k])
        mw1,mw2,mw3=w1,w1+w2,w1+w2+w3
        mw1index,mw2index,mw3index=[0],[0,k],[0,k,2*k]#mw1,mw2,mw3's index.
        for i in range(1,len(nums)-3*k+1):#last index for w1 window will be n-3k
            w1+=nums[i-1+k]-nums[i-1]
            w2+=nums[i-1+2*k]-nums[i-1+k]
            w3+=nums[i-1+3*k]-nums[i-1+2*k]
            if w1>mw1:
                mw1,mw1index=w1,[i]
            if mw1+w2>mw2:
                mw2,mw2index=mw1+w2,mw1index+[i+k]
            if mw2+w3>mw3:
                mw3,mw3index=mw2+w3,mw2index+[i+2*k]
        return mw3index

# Time: O(N)
# Space:O(1)



        
# DP 

# offical solution using DP
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/solution/

# other solution using DP
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/849710/Python-top-down-DP-in-various-forms

'''
DP problem similar to Buy and Sell Stock
H0[i] means the max sum at nums[i] when the first index is choosen.
H1[i] means the max sum at nums[i] when the second index is choosen.
H2[i] means the max sum at nums[i] when the third index is choosen.
Build a prefixSum array, PreSum[i] = sum(nums[:i])
H0[i] = max(H0[i-1], PreSum[i+k]-PreSum[i])
H1[i] = max(H1[i-1], H0[i-k]+PreSum[i+k]-PreSum[i])
H2[i] = max(H2[i-1], H1[i-k]+PreSum[i+k]-PreSum[i])
For H0, iterate i from 0 to len(nums)-k
For H1, iterate i from k to len(nums)-k
For H2, iterate i from 2*k to len(nums)-k
Track the index of each choice.
Time: O(n)
Space: O(n)
'''

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        len_nums = len(nums)
        PreSum = [0]
        for n in nums:
            PreSum += [n+PreSum[-1]]
        
        H0, H1, H2 = [-1] * len_nums, [-1] * len_nums, [-1] * len_nums
        idx0, idx1, idx2 = [None] * len_nums, [None] * len_nums, [None] * len_nums        
        for i in range(len_nums-k+1):
            add = PreSum[i+k]-PreSum[i]
            H0[i] = add
            idx0[i] = [i]
            if i > 0 and H0[i-1] >= H0[i]:
                H0[i] = H0[i-1]
                idx0[i] = idx0[i-1]
            if i >= k:
                H1[i] = H0[i-k] + add
                idx1[i] = idx0[i-k] + [i] 
                if i > k and H1[i-1] >= H1[i]:
                    H1[i] = H1[i-1]
                    idx1[i] = idx1[i-1]
            if i >= 2*k:
                H2[i] = H1[i-k] + add
                idx2[i] = idx1[i-k] + [i]
                if i > 2*k and H2[i-1] >= H2[i]:
                    H2[i] = H2[i-1]
                    idx2[i] = idx2[i-1]
                    
        return idx2[len_nums-k]


# Time: O(N)
# Space:O(N)






