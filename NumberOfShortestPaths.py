#Exercise 3: Use recursion to calculate the number of shortest paths from the bottom left to the top right corner in an X x Y grid
# Implement a function nsp with two parameters s.t. nsp(x,y) 
# calculates the number of shortest paths in a image missing-grid. 
# E.g. nsp(3,2) should return 10.
#  Hint: The number of paths in any middle position is the sum of the number of paths of the point to the left and the point below

#NAIVE RECURSIVE SOLUTION

def NSP(x,y):
    if x ==1 or y == 1 or (x == 1 and y == 1):
        return x + y
    else:
        return NSP(x,y-1) + NSP(x-1,y)

#MEMOIZED RECURSION

def NSPmemo(x,y,memo=None):
    if memo is None:
        memo = {}
    key = (x,y)
    if  key in memo:
        return memo[key]
    if x ==1 or y == 1 or (x == 1 and y == 1):
        return x + y
    else:
        memo[key] = NSPmemo(n,m-1,memo) + NSPmemo(n-1,m,memo)
    return memo[key]