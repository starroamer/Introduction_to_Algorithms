# encoding:utf8


def knapsack(w, v, W):
    n = len(w)
    c = [[0] * (W + 1) for _ in xrange(n + 1)]
    b = [[0] * (W + 1) for _ in xrange(n + 1)]

    for i in xrange(1, n + 1):
        for j in xrange(1, W + 1):
            if w[i - 1] > j:
                c[i][j] = c[i - 1][j]
            else:
                new_v = c[i - 1][j - w[i - 1]] + v[i - 1]
                if new_v > c[i - 1][j]:
                    c[i][j] = new_v
                    b[i][j] = 1
                else:
                    c[i][j] = c[i - 1][j]

    return c[n][W], b


def knapsack_mem_optimize(w, v, W):
    n = len(w)
    prev_c = [0] * (W + 1)
    current_c = [0] * (W + 1)
    b = [[0] * (W + 1) for _ in xrange(n + 1)]

    for i in xrange(1, n + 1):
        prev_c, current_c = current_c, prev_c
        for j in xrange(1, W + 1):
            if w[i - 1] > j:
                current_c[j] = prev_c[j]
            else:
                new_v = prev_c[j - w[i - 1]] + v[i - 1]
                if new_v > prev_c[j]:
                    current_c[j] = new_v
                    b[i][j] = 1
                else:
                    current_c[j] = prev_c[j]

    return current_c[W], b


def print_knapsack_result(b, w, result, i, j):
    if i == 0:
        return
    if b[i][j] == 1:
        result.insert(0, i)
        print_knapsack_result(b, w, result, i - 1, j - w[i - 1])
    else:
        print_knapsack_result(b, w, result, i - 1, j)


def knapsack_test():
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    W = 10
    # max_value, b = knapsack(w, v, W)
    max_value, b = knapsack_mem_optimize(w, v, W)
    print "max value is: ", max_value
    result = []
    print_knapsack_result(b, w, result, len(w), W)
    print "choose items: ", ' '.join(map(str, result))


if __name__ == "__main__":
    knapsack_test()
