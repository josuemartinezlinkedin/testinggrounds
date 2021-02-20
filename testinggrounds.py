'''
first leetcode success twosum
# #nums = #[3,3]#[3,2,4] #[2,7,11,15]
# nums = [3,2,4]
# #target #=6 #9
# target = 6
#
#
# def sumtwo(nums, target):
#     for i in nums:
#         other = target - i
#         if other in nums:
#             if nums.index(i) != nums.index(other):
#                 return(nums.index(i), nums.index(other))
#             elif other == i:
#                 this = [n for n,val in enumerate(nums) if val==i]
#                 if len(this) == 2:
#                     return this
# sumtwo(nums,target)

'''
for n,val enumerate([3,5,6,4,1,1]):
    print(n,val)



def sumtwo(nums,target):
    for i in nums:
        other = target - 1
        if other in nums:
            if nums.index(i) != nums.index(other):
                return [nums.index(i), nums.index(other)]
            elif other ==i:
                this = [n for n,val in enumerate(nums)if val==i]
                if len(this)==2:
                    return this
sumtwo([3,3],6)


'''#####################
'''some dictionary practice'''

newdict = dict()
newdict[5] = 3,5,6,7,8
newdict[10] = 4,'o','k', 'cool'
newdict[3] = nums
newdict[13] = 0
print(newdict)
print(newdict.keys())
newdict[5]
###################
'''

'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            else:
                d[nums[i]] = i
'''
'''

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

nums = [-1,0,1,2,-1,-4]
nums2 = [1,2,-2,1]
target = 0
def findzeros(nums):
    this = []
    if len(nums) > 2:
        for i in nums:
            for j in nums[::-1]:
                for n in nums[1::]:
                    if i + j + n == 0:
                        this.append([i,n,j])
            newthis = list(set(tuple(sorted(sub)) for sub in this))
            alist = []
            for i in set(nums):
                for lists in answers:
                    pass
                for numbers in lists:s
                    if i == numbers:
                        alist.append(i)
                if len(alist)>=2:
                    return []
                else:
                    return newthis


findzeros(nums2)
answers =  [(-2,1,1)]
alist = []
for i in set(nums2):
    for lists in answers:
        pass
    for numbers in lists:
        if i == numbers:
            alist.append(i)
            if len(alist)>=2:
                return []



def newnew(nums):
    llist = []
    alist = []
    nums2 = sorted(set(nums))
    if len(nums2)<=2:
        return []
    elif len(nums2) == 3:
        if nums2[0] + nums2[1] + nums2[2] ==0:
            return [nums2[0] + nums2[1] + nums2[2]]
        else:
            return []
    else:
        nums = sorted(nums)
        one = 1
        while len(nums) > 1+one:
            a = nums[0]
            b= nums[one]
            c=nums[1 + one]
            if a + b + c == 0:
                llist.append([a,b,c])
                one +=1
            else:
                one +=1
                    # [-2,-1,0,0,1,1,2,]
                while len(nums) > 1 + one:
                    b = nums[one]
                    c = nums[1+one]
                    if a + b + c == 0:
                        llist.append([a,b,c])
                        one+=1
                        if len(nums) == nums[1+one]:
                            break



newnew(nums)
[-1,0,1,2,4]
nums = [-1,0,1,2,-1,-4]
nums2 = [1,2,-2,1]
-1 + 0 + 1
'''
[1,2,-2,-1]
Output
[[-2,1,1]]
Expected
[]
'''
