from typing import List

class Game:
    def entry(self, nums: List[int]) -> bool:
        num_list = [float(num) for num in nums] # convert eveything to float
        return self.dfs(num_list)

    def dfs(self, nums: List[float]) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return abs(nums[0] - 24.0) < 0.00001 #means it equals 24 or near enough

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): # combine operations between two neighboring numbers
                for operation in range(6):
                    next_list = self.do_operation(nums, i, j, operation)
                    if next_list and self.dfs(next_list):
                        return True
        return False

    def do_operation(self, nums: List[float], i: int, j: int, operation: int) -> List[float]:
        next_list = [nums[k] for k in range(len(nums)) if k != i and k != j]

        if operation == 0:
            next_list.append(nums[i] + nums[j])
        elif operation == 1:
            next_list.append(nums[i] - nums[j])
        elif operation == 2:
            next_list.append(nums[j] - nums[i])
        elif operation == 3:
            next_list.append(nums[i] * nums[j])
        elif operation == 4:
            if nums[j] != 0:
                next_list.append(nums[i] / nums[j])
            else:
                return []
        elif operation == 5:
            if nums[i] != 0:
                next_list.append(nums[j] / nums[i])
            else:
                return []

        return next_list