# encoding:utf8
"""
对于输入的矩阵A1，A2, ... An，计算矩阵链乘法的最优计算次序，使得需要进行的乘法次数最少
"""
import sys


def matrix_chain_order(p):
    """
    :param p: size of each matrix in matrix chain
    :return: min num of multiplication
    """
    n = len(p) - 1
    m = [[None for i in xrange(n)] for j in xrange(n)]
    s = [[None for i in xrange(n)] for j in xrange(n)]

    for i in xrange(n):
        m[i][i] = 0

    for l in xrange(1, n):  # l is length of chain minus 1
        for i in xrange(0, n - l):
            j = i + l
            for k in xrange(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if m[i][j] is None or q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s


def print_optimal_order(s, i, j):
    if i == j:
        sys.stdout.write("A%d" % i)
    else:
        sys.stdout.write("(")
        print_optimal_order(s, i, s[i][j])
        print_optimal_order(s, s[i][j] + 1, j)
        sys.stdout.write(")")


if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    # p = [5, 10, 3, 12, 5, 50, 6]
    m, s = matrix_chain_order(p)
    matrix_num = len(p) - 1
    print m[0][matrix_num - 1]
    print_optimal_order(s, 0, matrix_num - 1)
