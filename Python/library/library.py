

class Library:
    def __init__(self):
        self.name = "James"
        self.color = "Brown"
        self.cat = []
        print self.name
        print self.color

        self.cat.append(self.name)
        self.cat.append(self.color)
    def get_cat(self):
        return self.cat



class Printer:
    def __init__(self):
        print "Printer"
    def print_out(self):
        print self




