class Library:
    def __init__(self):
        print "Library!"
    def get_avg(self, n):
        total = 0
        for i in n:
            total += i
        avg = total/len(n)
        return avg

class Printer:
    def __init__(self):
        print "Printer!"
        self.data = 0

    def print_out(self):
        print "The average is " + str(self.data)