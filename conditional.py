age = int(input("Enter your age here :"))

if(age>=18):
    print("Your age is above the consent")

elif(age<0):
    print("This is invalid age")

elif(age==0):
    print("This is invalid age")

else:
    print("Your age is below the consent")

print("End Of Program")



a = 90
b = int(input("Guess the value :"))

if(b>90):
    print("It's greater value")

elif(b==90):
    print("Congratulations you guessed correct value")

else:
    print("It's smaller value")

# multiple if 

c = int(input("Enter your age here :"))
# if statement no. : 1
if(c%2 == 0):
    print("It's even")
# end of if statement no. : 1

# if statement no. : 2

if(c>=18):
    print("Your age is above the consent")

elif(c<0):
    print("This is invalid age")

elif(c==0):
    print("This is invalid age")

else:
    print("Your age is below the consent")

# end of if statement no. : 2

print("End Of Program")
