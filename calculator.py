print ("| Welcome to Calculator Application |\n")

print("------------------------------\n")

ope = int(input("Enter number for the operation (1 to Addition, 2 to Subtract, 3 to Multiply, 4 to Divide, 5 to Modulus): "))

print ("\n")
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print ("\n")

if ope == 1 :
    result = num1 + num2
    print ("Addition:",num1,"+",num2,"=",result)

elif ope == 2 :
    result = num1 - num2
    print ("Subtract:",num1,"-",num2,"=",result)

elif ope == 3 :
    result = num1 * num2
    print ("Multiple:",num1,"*",num2,"=",result)
    
elif ope == 4 :
    result = num1 / num2
    print ("Divide:",num1,"/",num2,"=",result)
    
elif ope == 5 :
    result = num1 % num2
    print ("Modulus:",num1,"%",num2,"=",result)
    
else:
    print ("Invalide Operation")
    

