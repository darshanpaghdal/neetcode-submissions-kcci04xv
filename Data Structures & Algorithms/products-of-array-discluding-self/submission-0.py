class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        all_product = 1
        output = []
        is_zero = False
        is_multi_zero = False
        for ele in nums:
            if ele != 0:
                all_product *= int(ele)
            else:
                if is_zero:
                    is_multi_zero = True
                is_zero = True
        



        for ele in nums:

            if is_multi_zero:
                output.append(0)


            elif is_zero:
                if ele == 0:
                    output.append(all_product)
                else:    
                    output.append(0)

            else:
                output.append(all_product // int(ele))

            
        return output
        