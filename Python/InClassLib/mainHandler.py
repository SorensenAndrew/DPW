from library import *

class Main:
    def __init__(self):
        print "Main!"
        self.library = Library()
        self.printer = Printer()
        grades = [37,78,1126]
        avg = self.library.get_avg(grades)
        self.printer.data = avg
        self.printer.print_out()

main = Main()

