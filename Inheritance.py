# Inheritance in Python
class Parent:
    parentAtrr = 100

    def __init__(self):
        print("Parent Constructor")

    def parentMethod(self):
        print("Parent Method")

    def setAttr(self, attr):
        Parent.parentAtrr = attr
    
    def getAttr(self):
        print("Parent Attr: ", Parent.parentAtrr)

    def myMethod(self):
        print("myMethod Parent")

class Child(Parent):
    def __init__(self):
        print("Child Constructor")

    def childMethod(self):
        print("Child Method")
    
    def myMethod(self):
        print("myMethod Child")

# Data Hiding
class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

# main program
if __name__ == "__main__":
    c = Child()
    c.childMethod()
    c.myMethod()
    c.parentMethod()
    c.setAttr(200)
    c.getAttr()

    counter = JustCounter()
    counter.count()
    counter.count()
    print (counter.__secretCount)