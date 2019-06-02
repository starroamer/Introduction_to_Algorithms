# encoding: utf8


def longest_palindrome_sub_sequence(s):
    n = len(s)
    c = [[0] * n for _ in xrange(n)]
    b = [[0] * n for _ in xrange(n)]

    # calculate lps  of substring s[i:j+1] for all possible 0 <= i <= n and j >= i
    for l in xrange(1, n + 1):          # l is length of substring
        for i in xrange(n - l + 1):     # i is start of substring
            j = i + l - 1               # j is end of substring
            if j == i:
                c[i][j] = 1
                b[i][j] = 0
            elif j == i + 1:
                if s[i] == s[j]:
                    c[i][j] = 2
                    b[i][j] = 1
                else:
                    c[i][j] = 1
                    b[i][j] = 2
            elif s[i] == s[j]:
                c[i][j] = c[i + 1][j - 1] + 2
                b[i][j] = 3
            else:
                if c[i][j - 1] > c[i + 1][j]:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = 4
                else:
                    c[i][j] = c[i + 1][j]
                    b[i][j] = 5

    return c, b


def print_lps(s, b, i, j, result):
    if b[i][j] == 0 or b[i][j] == 2:
        result.append(s[i])
    elif b[i][j] == 1:
        result.append(s[i])
        result.insert(0, s[i])
    elif b[i][j] == 3:
        print_lps(s, b, i + 1, j - 1, result)
        result.append(s[i])
        result.insert(0, s[i])
    elif b[i][j] == 4:
        print_lps(s, b, i, j - 1, result)
    elif b[i][j] == 5:
        print_lps(s, b, i + 1, j, result)


def lps_test():
    s = "character"
    n = len(s)
    c, b = longest_palindrome_sub_sequence(s)
    lps = []
    print_lps(s, b, 0, n - 1, lps)
    print c[0][n - 1]
    print "".join(lps)


if __name__ == "__main__":
    lps_test()
