#activity 1 and or operators

a = 10
b = 8
c = 0

if a and b and c:
    print("all the numbers have boolean true")
else:
    print("atleast one number has boolean value false")

d = 10
e = -10
f = 0

if d > 0 or e > 0:
    print("either of the numbers are greater than 0")
else:
    print("no number is greater than 0")

# activity 2 not operators

t = 10
o = 12
s = 12

print(t != o)
print(o != s)

m = "coding"
n = "programmming"
if m != n:
    print(m ,'and', n,'are diffrent')

l = 10
p = 40

if (l==1) != (p==40):
    print("hello :)")

x = int(input("enter a number:"))
if x%2 != 0:
    print("the number is odd")
else:
    print("the number is even")

#activity 3 check BMI
height = float(input("enter height in cm:"))
weight = float(input("enter weight in kg:"))
BMI = weight / (height/100)**2

print("your BMI is:", BMI)

if BMI <= 18.4:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are healhty")
elif BMI <= 29.9:
    print("you are overweight")
elif BMI <= 34.9:
    print("you are serverly overweight")
elif BMI <= 39.9:
    print("you are obese")
else:
    print("you are severly obese")