
# from unittest import case


try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))

    print ("what kinda operation u wanna perform :\n press + for addition \n press - for subtraction \n press / for division \npress * for multiplication " )  

    o= (input("enter operation:"))
    match o:
        case "+":
            print(f"the sum of {a} and {b} is {a+b}")
        case "-":
            print(f"the difference of {a} and {b} is {a-b}")                    
        case "*":           
            print(f"the product of {a} and {b} is {a*b}")     
        case "/":
            if b==0:
                print("division by zero is not allowed")
            else:
                print(f"the quotient of {a} and {b} is {a/b}")

except Exception as e:
    print("invalid input",e)
