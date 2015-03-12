from library import *

class MainHandler:
    def __init__(self):
        self.m = Library()
        self.v = Printer()
        cat = self.m.get_cat()
        self.v.animal = cat
        self.v.print_out()

h = MainHandler()




