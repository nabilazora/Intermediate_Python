# Iterator from fruitstuple and print each value
# fruitstuple = ("banana", "lemon", "apple")
# newit = iter(fruitstuple)

# print(next(newit))
# print(next(newit))
# print(next(newit))

# Iterator from sequence of characters
# fruitstr = "lemon"
# newit = iter(fruitstr)

# print(next(newit))
# print(next(newit))
# print(next(newit))
# print(next(newit))
# print(next(newit))


# for Loop to iterate through a tuple

# fruitstuple = ("banana", "lemon", "apple")

# for i in fruitstuple:
#     print(i)

# for Loop to iterate through a string
# fruitstr = "lemon"

# for i in fruitstr:
#     print(i)

# Build an iterator that return numbers
# class Counting:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self) :
#         x = self.a
#         self.a += 1
#         return x

# newObj = Counting()        
# newit = iter(newObj)

# print(next(newit))
# print(next(newit))
# print(next(newit))
# print(next(newit))
# print(next(newit))
# print(next(newit))

# Build an iterator that return numbers with raise StopIteration
class Counting:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self) :
        if self.a <= 19:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

newObj = Counting()        
newit = iter(newObj)

for x in newit:
    print(x)