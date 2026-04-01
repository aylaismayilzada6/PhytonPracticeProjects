def add(*args):
    #print(args[3])
    sum = 0
    for n in args:
        sum += n
    return sum

#print(add(1,2,3,4))


#*
# Default  values in arguments when you don't have to init
# a val for each arg
# also we have unlimited functions
#  def add(*args) // this function can accept any number of arguments
# Another option is to use **kwargs unlimited arguments
#

# Another option is to use **kwargs unlimited arguments
def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #

calculate(2, add=3, multiply= 5) #this basically creates a dictionary

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="nissan", model="gtr")
print(my_car.model, my_car.make)
