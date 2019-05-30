# encoding:utf8
"""
计算最长公共子序列
"""

import sys


def lcs_length(x, y):
    """
    calculate lcs's length of x and y
    :param x, y: given sequence
    :return:
    """
    m = len(x)
    n = len(y)

    # 下标从0到m、n，简化边界处理
    c = [[0] * (n + 1) for i in xrange(m + 1)]
    b = [[0] * (n + 1) for i in xrange(m + 1)]

    for i in xrange(1, m + 1):
        for j in xrange(1, n + 1):
            if x[i - 1] == y[j - 1]:
                # 这里i,j如果从0开始，就需要判断边界了
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "＼"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "←"

    return c, b


def print_lcs(x, b, i, j, result):
    if i == 0 or j == 0:
        return
    if b[i][j] == "＼":
        print_lcs(x, b, i - 1, j - 1, result)
        result.append(x[i - 1])
    elif b[i][j] == "↑":
        print_lcs(x, b, i - 1, j, result)
    else:
        print_lcs(x, b, i, j - 1, result)


def lcs_length_mem_optimize(x, y):
    """
    calculate lcs's length of x and y with low memeory use
    :param x, y: given sequence
    :return:
    """
    m = len(x)
    n = len(y)

    if m < n:
        x, y = y, x
        m, n = n, m

    c = [0] * n

    for i in xrange(0, m):
        prev = 0
        for j in xrange(0, n):
            if x[i] == y[j]:
                if j > 0:
                    current_lcs = c[j - 1] + 1
                else:
                    current_lcs = 1
            elif c[j] >= prev:
                current_lcs = c[j]
            else:
                current_lcs = prev

            if j > 0:
                c[j - 1] = prev
            prev = current_lcs
        c[j] = prev

    return c[j]


def lcs_test():
    x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    y = ['B', 'D', 'C', 'A', 'B', 'A']
    c, b = lcs_length(x, y)
    print c[len(x)][len(y)]
    for row in b:
        print ' '.join(map(str, row))

    result = []
    print_lcs(x, b, len(x), len(y), result)
    result.reverse()
    print " ".join(result)


def lcs_mem_optimize_test():
    # x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    # y = ['B', 'D', 'C', 'A', 'B', 'A']
    # x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    x = [1, 0, 0, 1, 0, 1, 0]
    y = [0, 1, 0, 1, 1, 0, 1, 1, 0]
    lcs_len = lcs_length_mem_optimize(x, y)
    c, b = lcs_length(x, y)
    lcs_len_2 = c[len(x)][len(y)]

    print lcs_len, lcs_len == lcs_len_2


def longest_increase_sub_sequence(a):
    n = len(a)
    b = [1] * n
    for i in xrange(n):
        for j in xrange(i):
            if a[j] < a[i]:
                b[i] = max(b[i], b[j] + 1)

    max_len = max(b)
    lis = []
    tar_get_len = max_len
    for i in xrange(n - 1, -1, -1):
        if b[i] == tar_get_len:
            lis.insert(0, a[i])
            tar_get_len -= 1

    return lis


def lis_test():
    a = [5, 6, 7, 1, 2, 8]
    lis = longest_increase_sub_sequence(a)
    print ' '.join(map(str, lis))


if __name__ == "__main__":
    # lcs_test()
    # lcs_mem_optimize_test()
    lis_test()
