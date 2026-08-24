
print ("Hello World")

#write a program to input 2 numbers and  print their sum

num1 = int(input("Enter your number : "))
num2 = int(input("Enter your number : "))
sum = (num1 + num2)
print(sum)




light = input("Light is : ")
if (light == "red"):
    print("STOP")
elif (light == "yellow"):
    print("WAIT")
elif (light == "green"):
    print("GO")
else:
    print("Light is broken ")



print("Student Grade-Card")
dms = float(input("Enter your marks of DMS : "))
se = float(input("Enter your marks of SOFTWARE ENGINEERING : "))
cn = float(input("Enter your marks of COMPUTER NETWORK  : "))
dbms = float(input("Enter your marks of DATABASE MANAGEMENT SYSTEM  : "))
cc = float(input("Enter your marks of CLOUD COMPUTING : "))

total = (dms + se + cn + dbms +cc ) 
print("Total is : ",total)
avg = (total )/ 5

score = int (avg)
print("Score is : ",score)

if (score>=90 and score<=100):
    print("Your Grade is : A")
elif(score>=80 and score<=89):
    print("Your Grade is : B")
elif(score>=70 and score<=79):
    print("Your Grade is : C")
elif(score>=60 and score<=69):
    print("Your Grade is : D")
else:
    print("Your Grade is : F")
