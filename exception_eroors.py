try:
    num1 = int( input("enter ther number1: "))
    num2 = int( input("enter the number2: "))
    r = num1/num2
    print(r)
except ZeroDivisionError as ex:
    print(ex)
except:print("An Errors")
finally:
    print("END")


 
