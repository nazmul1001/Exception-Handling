a=5
b=0
print("Resource open")
try:
    k=int(input("Please Enter a number "))
    
    print(a/b)
    print (k)

except ZeroDivisionError as e:
    print("You can't divide by zero.",e)

except ValueError as e:
    print("Invalid input. You entered a Letter",e)
    
except Exception as e:
    print("Something went wrong",e)


finally:
    print("Resource closed. Bye")
#Adding a comment