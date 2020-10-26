import sys
def knapsack(weights, capacity):
    n = len(weights)
    table = [[False] * (n+1) for x in range (capacity + 1) ]
    table[0][0] = True

    for i in range (1, n+1):
        for w in range (capacity + 1):
            if weights[i-1] > w:
                table[w][i] = table[w][i-1]
            else:
                table[w][i] = table[w][i-1] or table[w-weights[i-1]][i-1]
    i=capacity
    while i>=0:
        for val in table[i]:
            if val == True:
                return i
        i-=1

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    assert 1 <= W <= 10**4
    assert 1 <= n <= 300
    for wgt in w:
        assert 0<=wgt<=10**5
    print(knapsack(w, W))
