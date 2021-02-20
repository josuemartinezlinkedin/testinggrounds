class Computer: #to define your class you need a colon
        #here we need to include Variables
        #Behavior includes Methods(functions)
    def config(self): # method config since every computer has config
       print("i5m 16gb, iTB") #just some common config

com1 = Computer()
#We mention that com1 is an object of computer using a constructor ()
print(com1)
#to see what our com1 is we can use a type function
print(type(com1))

#now we want to see the config of our class
#To use a method we need to say object plus method then pass object
Computer.config(com1)
#Can also call a method using the object itself
com1.config()

"""summary define class
- give class Variable
- use a constructor to set an object to a Variable
- use class.method(pass the object)
- or use the object itself and call method passing itself as argument
"""

####
####
####
####
'''PART 2'''
class Comp:
    def __init__(self, cpu, ram):
        #this will be called automatically
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("Config is ", self.cpu, self.ram)

com1 = comp('i5', 16)
com2 = comp()
