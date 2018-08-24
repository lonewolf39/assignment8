# Q.1- Calculate area and circumference of a circle
class circle:
    def __init__(self):
        self.radius=10
    def getArea(self):
        self.area=3.14*(self.radius**2)
        print(self.area)
    def getcircumference(self):
        print(2*3.14*self.radius)
a=circle()
a.getArea()
a.getcircumference()

# Q.2- Make a class student and display its required info

class student:
    def __init__(self):
        self.name=input("Enter Name")
        self.rollno=int(input("Enter Rollno"))
        self.age=0
        self.marks=0
    def display(self):
        print("Student Info")
        print(self.name,self.rollno,self.age,self.marks)
    def setAge(self):
        self.age=int(input("Enter Age"))
    def setmarks(self):
        self.marks=int(input("Enter Marks"))
x=student()
x.setAge()
x.setmarks()
x.display()


# Q.3-Convert Temperature

class temperature:
    def __init__(self):
        self.ctemp=0
        self.ftemp=0
    def convertFahrenheit(self):
        self.ctemp=float(input("Enter temperature in celsius"))
        self.ftemp=self.ctemp*1.8+32
        print(self.ctemp,"celsius=",self.ftemp,"Fahrenheit")
    def convertcelsius(self):
        self.ftemp=float(input("Enter temperature in celsius"))
        self.ctemp=(self.ftemp - 32) * 0.5556
        print(self.ftemp,"Fahrenheit=",self.ctemp,"celsius")
x=temperature()
x.convertFahrenheit()
x.convertcelsius()

# Q.4- Create a class Moviedetails and perform the required functionalities

class MovieDetails:
    def Display(self):
        print("Movie Details:")
        print("Artist Name:-",self.artistname,"\nYear Of Release:-",self.year,"\nRating:-",self.rating)
    def Add(self):
        self.artistname=input("Enter Artist Name:- ")
        self.year=int(input("Enter year Of release:- "))
        self.rating=float(input("Enter The Rating"))
x=MovieDetails()
x.Add()
x.Display()
# Q.5- Inheritance(animal)

class animal:
    def info_(self):
        print("Animal Class")
class animal_attribute():
    def attribute(self):
        print("Animal_Attributes")
class tiger(animal,animal_attribute):
    def s(self):
        print("Tiger Class")
a=animal()
b=animal_attribute()
c=tiger()
c.info_()
c.attribute()

# Q.6- Determine the Output
output= A B
		A B


# Q.7- Inheritance(Shapes)
class shape:
    def method_area(self):
        self.length=int(input("Enter The length"))
        self.breadth=int(input("Enter the breadth"))
class rectangle(shape):
    def method_area(self):
        self.length=int(input("Enter The length of Rectangle"))
        self.breadth=int(input("Enter The breadth of rectangle"))
class square(shape):
    def method_area(self):
        self.length=int(input("Enter The length of sides of square"))
x=shape()
y=rectangle()
z=square()
y.method_area()
z.method_area()
