
print ("Hello World")

    # string with Escape Character
str1 = "Hello \ti am sumit parkar \ni am from kolhapur "
print(str1)




#string Concatenation
s1 = "Hello"
s2 = "World"
strr =(s1 +" "+ s2)
print(strr)

print(len(str1))
print(len(s1))
print(len(s2))
print(len(strr))


#write a program to input 2 numbers and  print their sum

num1 = int(input("Enter your number : "))
num2 = int(input("Enter your number : "))
sum = (num1 + num2)
print(sum)

#write a program  input 2 floating point  numbers  and print their average 
num1 = float(input("Enter your 1st number : "))
num2 = float(input("Enter your 2nd number : "))
sum = (num1 + num2)
print ("Your Sum is = ",sum)
avg = (sum / 2)
print("Your average is = ",avg)



#write a program  to input  side of a square  and print its area 
side = int(input("Enter your Side of squre : "))
area = (side * side)
print (area)



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


nums =  int(input("Enter your num : "))
if (nums %2 == 0):
    print("The num is Even")
elif(nums %2 != 0):
    print("The num is odd")




# write a program to find the greatest of 3 numbers entered by the user
n1 = int(input("Enter the number : "))
n2 = int(input("Enter the number : "))
n3 = int(input("Enter the number : "))

if (n1>=n2 and n1>=n3):
    print("The first number largest : ",n1)
elif(n2>=n1 and n2>=n3):
    print("The second number is largest : ",n2)
else:
    print("The third number is largest :",n3)

else :
    print("Invalid Input nums")



#write a program to check if a number is a multiple of 7 or not
num = int (input("Enter the number : "))
if(num %7 ==0):
    print("The number is multiple of 7 :",num)
else:
    print("The number is not multiple of 7")

i =1
while (i <= 10):
    print(i)
    i +=1
