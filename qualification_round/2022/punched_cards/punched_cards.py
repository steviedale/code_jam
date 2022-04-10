num_testcases = int(input())

for testcase_i in range(num_testcases):
    print(f'Case #{testcase_i+1}:')
    row_str, col_str = input().split(' ')
    row, col = int(row_str), int(col_str)
    for row_i in range(row):
        for col_i in range(col):
            if col_i == 0 and row_i == 0:
                print('..', end='')
            else:
                print('+-', end='')
        print('+') 
        for col_i in range(col):
            if col_i == 0 and row_i == 0:
                print('..', end='')
            else:
                print('|.', end='')
        print('|') 

    for col_i in range(col):
        print('+-', end='')
    print('+') 