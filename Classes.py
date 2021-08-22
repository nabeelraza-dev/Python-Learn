# Classes in Python
class Employee:

    empCount = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.first, self.last, ", Salary: ", self.pay)


emp1 = Employee("Zara", "Ali", 2000)
emp2 = Employee("Manni", "Ali", 5000)

print("Total Employee %d" % Employee.empCount)
emp1.displayEmployee()
emp2.displayEmployee()