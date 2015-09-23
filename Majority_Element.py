def majorityElement(nums):
    di = {}
    maxtimes = len(nums)/2
    for i in nums:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
        if di[i] > maxtimes:
            return di[i]
