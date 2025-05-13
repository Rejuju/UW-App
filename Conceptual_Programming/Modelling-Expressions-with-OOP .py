"""
class Expr:
	pass

class Constant(Expr):

	def __init__(self, val):
		self.val = val
	def __str__(self):
		return str(self.val)


class Var(Expr):
	def __init__(self, name):
		self.name=name
	def __str__(self):
		return self.name



class BinOp(Expr):
	def __init__(self,left, right):
		self.left = left
		self.right = right
class Times(BinOp):
    def __str__(self):
        return str(self.left)+"*"+str(self.right)
class Plus(BinOp):
    def __str__(self):
        return str(self.left)+"+"+str(self.right)

class Times(BinOp):
 
    def __str__(self):
        return "("+str(self.left)+"*"\
                +str(self.right)+")"
    
class Plus(BinOp):
     
    def __str__(self):
        return "("+str(self.left)+"+"+\
                str(self.right) +")"
    
## x*y+7

expr1 = Plus(Times(Var("x"),Var("y")),Constant(7))
            
##  x*(y+7)

expr2 = Times(Var("x"), Plus(Var("y"), Constant(7)))

print(expr1)
print(expr2)
Out:

((x*y)+7)
(x*(y+7))


"""

#Challenge: Given the above Classes and their methods, Adjust the Class Binop(Expr) so that unecessary brackets are removed

#Hint: There are some conventions in mathematics (not a rule), preceding rules… for example, times goes first than plus; Those conventions allows us to save brackets 



class Expr:
    
    def __str__(self) :
        return self.str_aux(0) #set the precedence of a null expression to 0 i.e. the parent most Class method is always 0

class BinOp(Expr):
        
    def __init__(self,left, right):
        self.left = left # left node of a binary tree
        self.right = right #right node of a binary tree

    def str_aux(self,prec) :
        
        s = self.left.str_aux(self.prec)+ self.op \
            +self.right.str_aux(self.prec) #make a recursive call to evaluate the precedence of a subexpression to its parent operator 

        if self.prec < prec : #We put brackets around a sub-expression (like 1+2) if its main operator (Plus, precedence 1) has lower precedence than the operator of the expression it's part of (Times, precedence 2)
            return "("+s+")"
        else : #just return the expression if the main operator has a higher precedence than the subexpression
            return s
                      
    def eval(self,env) : #eval method takes in the "env" variable which is just a dictionary to store variables and their values
        return self.fun(self.left.eval(env),\
                        self.right.eval(env))#returns the return value of the fun function, where the left and right branches 
                        # of the tree are passed as arugments for the x and y parameters respectively
 
class Times(BinOp):

    prec = 2 # set precedence for the Times Class
    op = "*" # Times Class variable for the multiplication symbol
    
    def fun(self,x,y) :
        return x*y #the function "fun" performs the multiplication and returns the result

class Plus(BinOp):
    
    # same comments as Times(BinOp) subclass

    op = "+" 
    prec = 1
    
    def fun(self,x,y) :
        return x+y

 #consonants and variables just return themselves   
        
class Constant(Expr):
    
    def __init__(self,value):
        self.value = value
    
    def str_aux(self,prec):
        return str(self.value)
    
    def eval(self,env) :
        return self.value

class Var(Expr):
    
    def __init__(self,name):
        self.name = name 
    
    def str_aux(self,prec):
        return self.name
    
    def eval(self,env) :
        return env[self.name]