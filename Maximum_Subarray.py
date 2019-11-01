class Solution:

    def trim(self, nums):
        if nums[0] < 0 and nums[-1] < 0:
            trimmed_nums = nums[1:-1]
            print('1: ', nums)
        elif nums[0] < 0 and nums[-1] >= 0:
            trimmed_nums = nums[1:]
            print('2: ', nums)
        elif nums[-1] < 0 and nums[0] >= 0:
            trimmed_nums = nums[:-1]
            print('3: ', nums)
        else:
            print('4: ', nums)
            trimmed_nums = nums
        return trimmed_nums

    def maxSubArray(self, nums):
        temp = nums
        while len(temp) > 3:
            temp = self.trim(temp)
            print('nums when enter while-loop: ', temp)
            head = sum(temp[0:2])
            tail = sum(temp[len(temp) - 2:])
            temp = [head] + temp[2:len(temp) - 2] + [tail]
            print('nums when exit while-loop', temp)
            print('-------------')

        temp = self.trim(temp)
        if len(temp) <= 1:
            print(temp)
            return max(nums)
        elif sum(temp) > max(nums):
            print(temp)
            return sum(temp)
        else:
            print(nums)
            return max(nums)


"""
class Solution:
    
    def trim(self, nums):
        print('initial nums: ', nums)
        print('\n\n')
        if nums[0] >= 0 and nums[-1] >= 0:
            print('1 ', nums)
            return nums
        else:
            if nums[0] < 0 and nums[-1] < 0:
                nums = nums[1:-1]
                print('2 ', nums)
            elif nums[-1] < 0 and nums[0] >= 0:
                nums = nums[:-1]
                print('3 ', nums)
            elif nums[0] < 0 and nums[-1] >= 0:
                nums = nums[1:]
                print('4 ', nums)
            return nums
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        temp = nums
        temp = self.trim(temp)
        
        while len(temp) > 3:
            print('nums when enter while-loop: ', temp)
            head = sum(temp[0:2])
            tail = sum(temp[len(temp)-2:])
            temp = [head] + temp[2:len(temp)-2] + [tail]
            print('nums when exit while-loop', temp)
            print('-------------')
            temp = self.trim(temp)
        if len(temp) == 0:
            return None
        elif len(temp) == 1:
            return temp[0]
        elif sum(temp) >= max(temp):
            return sum(temp)
        else:
            return max(nums)
"""

def main():
    a = Solution()
    b = a.maxSubArray([0, -3, 1, 1])
    c = a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    d = a.maxSubArray([0])
    print(b)
    print('******************')
    print(c)
    print('******************')
    print(d)
    return b, c


if __name__ == "__main__":
    main()
