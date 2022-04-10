num_testcases = int(input())

# %%
def find(l, q):
    for i, item in enumerate(l):
        if item == q:
            return i
    return None
# 10 10 7 7 7 6 5 4 4 4 
def solve(dice):
    dice = sorted(dice)
    table = [list(range(d)) for d in dice]
    best = 0
    while len(table) > 0:
        cur_num = None
        cur_counter = 0
        for rolls_i, rolls in enumerate(table):
            if cur_num is None:
                cur_num = rolls.pop(0)
                cur_counter += 1
            else:
                if cur_num+1 in rolls:
                    index = find(rolls, cur_num+1)
                    cur_num = rolls.pop(index)
                    cur_counter += 1
            if len(rolls) == 0:
                table.pop(rolls_i)
        best = max(cur_counter, best)
    return best 

# %%
for testcase_i in range(num_testcases):
    print(f'Case #{testcase_i+1}: ', end='')
    num_dice = int(input())
    dice = [int(x) for x in input().split()]
    x = solve(dice)
    print(x)