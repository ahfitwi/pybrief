------------------------------------------------------------------------------
#  OOP, Compiled by: Alem H Fitwi, 
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Intro
#------------------------------------------------------------------------------

# Object: a collection of data (vars) and methods (functions) that act on those
        # data. It is also an instance of a class.
# Instantiation (instantiate): the process of creating an instance or object
# Attribute:  a characteristic of an object 
# Method: an opration we can perform on the objects

## Types of variables and methods in OOP
#- Type of variables:
    #1. Instance variable
    #2. Class variable
#- Types of methods
    #1. Instance Method
        #- A. Accessor/getter Methods
        #- B. Mutator/setter Methods        
    #2. Class Method
        #- Works with class variables
    #3. Static Method  
        #- Works with neither class nor instance variables

#------------------------------------------------------------------------------
# Define A class
#------------------------------------------------------------------------------
class Sample:
    class_attribute = 9
    
    # Constructor/Dunder Init Method
    def __init__(self, instance_var1 = 9, instance_var2 =None):
        self.instance_var1 = instance_var1
        self.instance_var2 = instance_var2
    
    # Instance Method
    def inst_method1(self,val):
        if self.instance_var2 != None:
            return self.instance_var1 + val
        else:
            return None

    # Instance Method
    def inst_method2(self,val1, val2):
        return val1 + val2 + Sample.class_attribute
    # Class Method
    # Helper methods for initialization
    # A class method is a method that is bound to the class and 
    #   not the object of the class.
    # It can modify a class state that would apply across all the 
    #  instances of the class.
    # Can modify class state
    # We generally use class method to create factory methods. 
    #   Factory methods return class objects ( similar 
    #   to a constructor ) for different use cases.
    # cls parameter that points to the class—and not the object
    #  instance—when the method is called.

    @classmethod
    def class_method(cls):
        instance = cls(cls.class_attribute)
        cls.class_attribute += 1
        return instance
   
    # Static Method
    # To create utility functions.
    @staticmethod
    def static_method(a,b):
        return a + b
    

imeth = Sample(3,4)
cmeth = Sample.class_method()
smeth = Sample()
print(imeth.inst_method1(10)) #13
print(cmeth.class_attribute)#10
print(smeth.static_method(5,6)) #11

#------------------------------------------------------------------------------
# Usecase of a class method
#------------------------------------------------------------------------------
class A(object):
    value = 0
    def __init__(self, name):
        self.name = name

    @classmethod
    def produce(cls):
        instance = cls(cls.value)
        cls.value += 1
        return instance

class B(A):
    @classmethod
    def produce(cls):
        instance = super(B, cls).produce()
        instance.name = "B %s" % instance.name
        return instance

x = A.produce()
y = B.produce()

print(f"x.name: {x.name}")#0
print(f"A.value: {A.value}")#0
print(f"y.name: {y.name}")#1
print(f"B.value: {B.value}")#0
print(f"Everything is object in py, isinstance(x, object: {isinstance(x, object)}")
#Delete attribute: del num1.imag
#------------------------------------------------------------------------------
# Inheritance
#------------------------------------------------------------------------------
# Inheritance is a way to form new classes using classes that have already been 
# defined. The newly formed classes are called derived classes, the classes 
#   that we derive from are called base classes.
# Inheritance enables us to define a class that takes all the functionality 
# from a parent class and allows us to add more
# It allows:
#   Inherit functionalities of a base class
#   Extend the functionalities of a base class
#   Override the original attributes or methods

class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Animal Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")   

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("Cat created")

    def whoAmI(self):
        print("Cat")

    def bark(self):
        print("Meow!")  

print(f"--------------------------------------------------")
d = Dog()
c = Cat()
print(f"--------------------------------------------------")
print(f"isinstance(d, Dog): {isinstance(d, Dog)}")
print(f"isinstance(d, Animal): {isinstance(d, Animal)}")
print(f"isinstance(c, Cat): {isinstance(c, Cat)}")
print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")
print(f"issubclass(Cat, Animal): {issubclass(Cat, Animal)}")
print(f"--------------------------------------------------")

#------------------------------------------------------------------------------
# Class Method Names
#------------------------------------------------------------------------------
def methods(methods):
    def deco(f):
        f.methods = methods
        return f
    return deco

class Names:
    @methods('addvals')
    def addvals(a,b): 
        return a+b

    @methods('mulvals')
    def mulvals(a,b):
        return a*b

    @methods('subvals')
    def subvals(a,b):
        return a-b

    @methods('divvals')
    def divvals(a,b):
        return a/b

def get_methods(Class):
    method_lst = {}
    for name, attrib in vars(Class).items():
        if callable(attrib):
            methods = attrib.methods
            if methods not in method_lst:
                method_lst[methods] = []

            method_lst[methods].append(attrib)
    return method_lst

def exec_mthd(func, *args):
    return func(*args)


print(f"Method Names: {get_methods(Names)}")

lsts = ['addvals', 'mulvals', 'subvals','divvals']

mnames = get_methods(Names)
for m in lsts:
    print(f"{mnames[m][0]}: {exec_mthd(mnames[m][0], 10,2)}")

print(f"--------------------------------------------------")

#------------------------------------------------------------------------------
# Ploymorphism
#------------------------------------------------------------------------------
# polymorphism refers to the way in which different object classes can share 
# the same method name,
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):    # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())
print(f"--------------------------------------------------")

#------------------------------------------------------------------------------
# Dunder Methods: init, str, len, del
#------------------------------------------------------------------------------
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s,\nAuthor: %s,\nPages: %s"\
                %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)
#Special Methods
print(book)
print(len(book))
del book
print(f"--------------------------------------------------")

#------------------------------------------------------------------------------
# Multiple and Multilevel Inheritance
#------------------------------------------------------------------------------
#Mulitple
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

# Multilevel
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass

#------------------------------------------------------------------------------
# MRO
#------------------------------------------------------------------------------
class A:
    num = 4
    
class B(A):
    pass

class C(A):
    num = 5
    
class D(B,C):
    pass
#Schematically, the relationship looks like this:
#        A
#       num=4
#      /     \
#     /       \
#     B       C
#    pass   num=5
#     \       /
#      \     /
#         D
#       pass
print(f"D.num:{D.num}")
print(f"--------------------------------------------------")

#super()
#Python's built-in super() function provides a shortcut for 
#  calling base classes, because it automatically follows 
#  Method Resolution Order.
# In its simplest form with single inheritance, super() can 
# be used in place of the base class name.
# In a more dynamic form, with multiple inheritance like 
# the "diamond diagram" shown above, super() can be used to 
# properly manage method definitions:

class A:
    def truth(self):
        return 'All numbers are even!'
    
class B(A):
    def truth(self):
        return 'Some numbers are odd & divisible by 3!'

class C(A):
    def truth(self):
        return 'Some numbers are even!'  

class D(B,C):
    def truth(self,num):
        if num%2 == 0 and num > 0:
            return A.truth(self)
        elif num%2 == 1 and num%3 == 0:
            return B.truth(self)
        else:
            return super().truth() 
#------------------------------------
d = D()
print("d.truth(5)",d.truth(5))
print("d.truth(6)",d.truth(6))
print("d.truth(-4)",d.truth(-4))

class A:
    def truth(self):
        return 'All numbers are even!'
    
class B(A):
    def truth(self):
        return 'Some numbers are odd & divisible by 3!'

class C(A):
    def truth(self):
        return 'Some numbers are even!'  

class D(B,C):
    def truth(self,num):
        if num%2 == 0 and num > 0:
            return A.truth(self)
        elif num%2 == 1 and num%3 == 0:
            return B.truth(self)
        else:
            return super().truth() 
#------------------------------------
d = D()
print("d.truth(5)",d.truth(5))
print("d.truth(6)",d.truth(6))
print("d.truth(-4)",d.truth(-4))

class A:
    def truth(self):
        return 'All numbers are even!'
    
class B(A):
    def truth(self):
        return 'Some numbers are odd & divisible by 3!'

class C(A):
    def truth(self):
        return 'Some numbers are even!'  

class D(B,C):
    def truth(self,num):
        if num%2 == 0 and num > 0:
            return A.truth(self)
        elif num%2 == 1 and num%3 == 0:
            return B.truth(self)
        else:
            return super().truth() 
#------------------------------------
d = D()
print("d.truth(5)",d.truth(5))
print("d.truth(6)",d.truth(6))
print("d.truth(-4)",d.truth(-4))

print("MRO: d.mro()", D.mro())
# d.truth(5) Some numbers are odd & divisible by 3!
# d.truth(6) All numbers are even!
# d.truth(-4) Some numbers are odd & divisible by 3!

print(f"--------------------------------------------------")
# Demonstration of MRO
print('MRO Demo:')
class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
# [<class '__main__.M'>, <class '__main__.B'>, 
# <class '__main__.A'>, <class '__main__.X'>, 
# <class '__main__.Y'>, <class '__main__.Z'>, 
# <class 'object'>]
#
print(f"--------------------------------------------------")
#------------------------------------------------------------------------------
#                                        ~END~
#------------------------------------------------------------------------------
