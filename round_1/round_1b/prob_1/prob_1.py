# %%
import os
import numpy as np

# %%
# test_case = '/Users/sdale/repos/code_jam/round_1/round_1b/prob_1/testcases/1_input.txt'
# assert(os.path.exists(test_case))
# with open(test_case) as f:
#     input_lines = f.readlines()
# input_line_index = 0
# def input():
#     global input_line_index
#     ret = input_lines[input_line_index].replace('\n', '')
#     input_line_index += 1
#     return ret 

# %%
num_testcases = int(input())

# %%
def get_answer(pancakes):
    count = 0
    max_val = -float('inf')
    while len(pancakes) > 0:
        if pancakes[0] < pancakes[-1]:
            i = 0
        else:
            i = -1
        if pancakes[i] >= max_val:
            max_val = pancakes[i]
            count += 1
        pancakes.pop(i)
    return count

# %%
for testcase_i in range(num_testcases):
    input()  # number of pancakes (don't need)
    nums = [int(x) for x in input().split()]
    ans = get_answer(nums)
    print(f'Case #{testcase_i+1}: {ans}')

# %%



