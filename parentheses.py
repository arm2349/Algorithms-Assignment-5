input = input()
### ARITHMETIC EXPRESSION ###

#CONVERT INPUT
def convert_input(s):
    nums = []
    ops = []
    valid_ops = ["-", "+", "*"]
    for n in s:
        if n in valid_ops:
            ops.append(n)
        else:
            nums.append(int(n))
    return nums, ops

#EVALUATE PROCEDURE
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

#CREATE MATRIX
def create_square_matrix(n, starting_value=None):
    matrix = [[starting_value for x in range (n)] for x in range (n)]
    return matrix

#MIN AND MAX PROCEDURE
def min_and_max(i, j, op, m, M):
    minimum = float('inf')
    maximum = float('-inf')
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return (minimum, maximum)



#GET MAXIMUM VALUE
def get_max_value(s):
    nums_and_ops = convert_input(s)
    numbers = nums_and_ops[0]
    operations = nums_and_ops[1]
    n = len(numbers)
    m = create_square_matrix(n)
    M = create_square_matrix(n)
    for i in range(n):
        m[i][i] = numbers[i]
        M[i][i] = numbers[i]
     ##used to be for s in range(n-1)
    for s in range(1,n):
        for i in range (0, n-s):
            j = i+s
            m[i][j], M[i][j] = min_and_max(i,j, operations, m, M)
    return M[0][n-1]
if __name__ == "__main__":
    print(get_max_value(input))
