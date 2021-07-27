# create generator function
# def Items():
#     print("First item!")
#     yield 15

#     print("Second item!")
#     yield 25

#     print("Last item!")
#     yield 40

# newGenerat = Items()

# print(next(newGenerat))
# print(next(newGenerat))
# print(next(newGenerat))

# return a value and terminates the execution of the function
# def Items():
#     print("First item!")
#     yield 15

#     return

#     print("Second item!")
#     yield 25

#     print("Last item!")
#     yield 40

# newGenerat = Items()

# print(next(newGenerat))
# print(next(newGenerat))
# print(next(newGenerat))

# Using generator function with for Loop
# def newUpTo(x):
#     for i in range(x):
#         yield i

# seq1 = newUpTo(7)
# print(next(seq1))
# print(next(seq1))
# print(next(seq1))
# print(next(seq1))
# print(next(seq1))
# print(next(seq1))
# print(next(seq1))

# yield square of number
# def squareSequence(x):
#     for i in range(x):
#         yield i * i

# newGenerat = squareSequence(9)        
# while True:
#     try:
#         print("Received on the next(): ", next(newGenerat))
#     except StopIteration:
#         break

# generator with for Loop and StopIteration automatically
def squareSequence(x):
    for i in range(x):
        yield i * i

newGenerat = squareSequence(9)        

for sqr in newGenerat:
    print(sqr)  