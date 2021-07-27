# Local scope of a function
# def newfunc():
#     x = 200
#     print(x)

# newfunc() 
# print(x)   

# Local variable can be accessed from a function inside function function
# def newOut():
#     x = 200
#     def newIn():
#         print(x)
#     newIn()

# newOut()

# Global variables are available from within any scope
# x =100

# def newfunc():
#     print(x)

# newfunc()    
# print(x)


# Naming and Renaming Variables
# x = 100

# def newfunc():
#     x = 50
#     print(x)

# newfunc()    

# print(x)

# The global keyword makes the variable global
x = 100

def newfunc():
    global x
    x = 50

newfunc()    

print(x)