class BruteForce:
    def majorityElement(nums-> List[int]) -> int:
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num
class HashMap:
    def majorityElement(nums):
        counts = {}
        for num in nums:
            # Increment the count for num in the dictionary, if num is not in the dictionary set it to 1
            counts[num] = counts.get(num, 0) + 1
            # If the count for num is greater than half the length of the list, return num as the majority element
            if counts[num] > len(nums) // 2:
                return num
            
class Sorting:
    def majorityElement(nums):
        # Sort the array
        nums.sort()
        # Return the middle element
        return nums[len(nums) // 2]

class BoyerMoore:
    def majorityElement(nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate