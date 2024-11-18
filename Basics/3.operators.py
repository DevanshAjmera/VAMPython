"""
#Arithematic Operators (+,-,*,/,//,%,**)
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=a/b                            #divide always gives float value
c
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=a//b                          # floor division gives integer value
c
a**b   # means a to the power b.
"""



#Assignment operator (=,+=,-=,*=,/=,//=,%=,**=)
a=10
a//=10       #gives int value and value that is less than or equal to float value
print(a)

x,y = 12,-5
print(x/y)   # -2.4
print(x//y)  # -3  



"""
#Comparison / Relational Operators (==,<,>,<=,>=,!=)
c=10
d=20
c!=d
"""



#Logical operator (and,or,not)
#and --- if any condition is false, it gives false
# answer in true,flase or 0 and 1 as per condition
# gives last no. if both are true ....
print(False and True)

# or -- if any is true gives true...
# answer in true,flase or 0 and 1 as per condition
print(10 or 50)

# not --- gives revert
# gives answer in t/f only
print(not(-50))




# Identity operator(is, is not)
# Membersip Operator (in, not in)
# Bitwise Operator (&,|,^)