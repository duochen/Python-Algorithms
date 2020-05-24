class stringADT:
    def __init__(self, str):
        self.str = str

    def upper(self):
        return self.str.upper()

    def lower(self):
        return self.str.lower()

    def length(self):
        return len(self.str)

    def display(self):
        print(self.str)

##########################################

s = stringADT("Hello World")
print(s.upper())
print(s.lower())
print(s.length())
s.display()
