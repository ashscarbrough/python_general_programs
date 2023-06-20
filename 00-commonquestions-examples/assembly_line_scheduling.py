def fun(a, t, cl, cs, x1, x2, n):
    # base case
    if cs == n - 1:
        if cl == 0:  # exiting from (current) line =0
            return x1
        else:  # exiting from line 2
            return x2
    # continue on same line
    same = fun(a, t, cl, cs + 1, x1, x2, n) + a[cl][cs + 1]
    # continue on different line
    diff = fun(a, t, not cl, cs + 1, x1, x2, n) + a[not cl][cs + 1] + t[cl][cs + 1]
    return min(same, diff)

n = 4  # number of stations
a = [[4, 5, 3, 2], [2, 10, 1, 4]]  # time taken at each station
t = [[0, 7, 4, 5], [0, 9, 2, 8]]  # time taken to switch lines
e1 = 10  # time taken to enter first line
e2 = 12  # time taken to enter second line
x1 = 18  # time taken to exit first line
x2 = 7  # time taken to exit second line
 
# entry from 1st line
x = fun(a, t, 0, 0, x1, x2, n) + e1 + a[0][0]
# entry from 2nd line
y = fun(a, t, 1, 0, x1, x2, n) + e2 + a[1][0]

print(min(x, y))
