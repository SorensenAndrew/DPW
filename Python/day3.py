class Student:
    def __init__(self, n):
        print "student created"
        self.name = n
        self.gender = ""
        self.grades = []

    def getAvg(self):
        total = 0
        for i in self.grades:
            total += i
        return total/len(self.grades)

john = Student("John")
john.grades = [70,80,90]
print john.getAvg()
print  john.name


# Import
# from "file name" import "class"
# * in class argument imports all from that file