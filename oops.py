#Class -> is collection of objects and functions...
# rules: 1st letter is in uppercase
class Devansh:
    print("My name is Devansh Ajmera.")
    age=18;
    email = "devanshajmera10@gmail.com"

#object creation
devansh : Devansh = Devansh() 
print("My age is",devansh.age)


class Student:
    name = "Devansh"
    email = "d@gmail.com"
    def findMyAge(this, cY, bY):      #this -> passes current class reference...
        ageInYear = cY-bY
        print(ageInYear)
    def Monthly_Pocket_Money(this,weekly_money):
        print("Monhly pocket money is",weekly_money*4)
stu : Student = Student()
stu.findMyAge(2024,2005)
stu.Monthly_Pocket_Money(200)