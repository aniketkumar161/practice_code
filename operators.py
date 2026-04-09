# 1 ARITHMETIC OPERATOR

a = int(input("enter first number : "))
b = int(input("enter second number : "))

print("addition =",a+b)
print("subtraction =",a-b)
print("multiplicaton =",a*b)
print("division =",a/b)
print(" modulus =",a%b)
print("power =",a**b)



# 2 RELATIONAL OPERATOR

a = int(input("enter first number : "))
b = int(input("enter second number : "))

print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)


#3 ASSIGNMENT OPERATOR

num = 10
num += 4
print ('num  :',num)

num = 10
num %= 4
print ('num  :',num)

num = 10
num *= 4
print ('num  :',num)

num = 10
num /= 4
print ('num  :',num)


#4LOGICAL OPERATOR 

print(not False )
print(not True)

#NOT(opposite realtion)
a=50
b=30
print(not False )
print(not(a>b))

#AND (if both value are true it will true)
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter")

#OR (if any one true it will true)

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It is weekend")
