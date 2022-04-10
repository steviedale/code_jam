required_units = 1e6

# %%
num_testcases = int(input())

# %%
def get_colors():
    c1, c2, c3, c4 = input().split(' ')
    return int(c1), int(c2), int(c3), int(c4)

for testcase_i in range(num_testcases):
    print(f'Case #{testcase_i+1} ', end='')
    # %%
    printers = [get_colors() for _ in range(3)]

    # %%
    recipe = []
    total = 0
    for color_i in range(4):
        min_units = float('inf')
        for printer in printers:
            min_units = min(printer[color_i], min_units)
        total += min_units
        recipe.append(min_units) 

    # %%
    if total > required_units:
        excess = total - required_units
        for i in reversed(range(len(recipe))):
            if excess > recipe[i]:
                excess -= recipe[i]
                recipe[i] = 0
            else:
                recipe[i] -= excess
                excess = 0
                break

    # %%
    if total < required_units:
        print('IMPOSSIBLE', end='')
    else:
        for i, ingredient in enumerate(recipe):
            print(int(ingredient), end='')
            if i < len(recipe) - 1:
                print(' ', end='')
    print() 