#1
class car:
    def __init__(self, color):
        self.color = color

    def car_color(self):
        print(f'My car is {self.color}')

car1 = car('red')
car2 = car('blue')
car1.car_color()
car2.car_color()
# Anna-correct

#2
class string_:
    def __init__(self, text):
        self.text = text

    def print_String(self):
        print(self.text.upper())

text1 = string_('Some text')
text1.print_String()
# Anna-correct

#3
#  import string -ANNA
class files:
    def create_file(self):
        import string
        alphabet = string.ascii_lowercase
        for letter in alphabet:
            with open(letter + ".txt", 'w+') as f:
                f.write(letter)

file1 = files()
file1.create_file()
# Anna-correct. As a rule, import string or other modules used outside of the class



