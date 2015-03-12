class Person:
    def __init__(self):
        print "Person Created"
        self.name = "Bob"
        self.ssn = 2345678901
        self.language = "English"

    def talk(self):
        print self.name + " is speaking in " + self.language

class Student(Person):
    def learn(self):
        print self.name + " is learning"
    def attend(self):
        print self.name + " is in class"
    def talk(self):
        print self.name + " is speaking " + self.language + ", intelligently"

stud1 = Student()
stud1.name = "Billy"
stud1.language = "Portuguese"

stud2 = Person()
stud2.name = "Harriet"
stud2.language = "Vietnamese"

stud1.talk()
stud1.attend()

stud2.talk()

