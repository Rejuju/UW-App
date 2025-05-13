#The key to solving any recursive problem is to find the base case and the recursive case.
#The base case is the simplest version of the problem
#The recursive case is the version of the problem that is reduced in size.
#The recursive case should call the function itself with a smaller version of the problem until it reaches the base case.

#Hanoi problem with recursion

def hanoiRec(n,f,h,t) :
    """
    parameters:  n, f, h, t
    n is the number of discs, f is the from tower, h is the helper tower and t is the target tower. 
    """

    #Base case: if n==0, return ... this pops the call from the stack
    if n==0 :
        return
    else :
        #Recursive call
        hanoiRec(n-1,f,t,h)#move n-1 discs from f to h using t as helper
        print("Move disc from {} to {}".format(f,t))#move the nth disc from f to t
        hanoiRec(n-1,h,f,t)#move n-1 discs from h to t using f as helper


#Solving the Hanoi Problem without recursion, using a stack to simulate the call stack (naive I know but this really helped me understand how the stack functions)
def hanoiImperative(n,f,h,t) :
    
    """
    parameters:  n, f, h, t
    n is the number of discs, f is the from tower, h is the helper tower and t is the target tower. 
    """

    stack = [["h",n,f,h,t]]
    while stack != [] :
        op = stack[0]
        stack = stack[1:]
        if op[0]=="h" :
            n,f,h,t = op[1],op[2],op[3],op[4]
            if n==0 :
                continue
            else :
                stack = [["h",n-1,f,t,h],
                         ["m",f,t],
                         ["h",n-1,h,f,t]]+stack
        elif op[0] == "m" :
            f,t = op[1],op[2]
            print("Move disc from {} to {}".format(f,t))

