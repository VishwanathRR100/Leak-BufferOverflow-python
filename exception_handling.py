try:
    inp = int(input("Enter a number: "))
    den = int(input("Enter a den: "))
    result = inp/den
except ZeroDivisionError as e:
    print(e)
    print("you cannot divide by zero..")
except ValueError as e:                     # eg : 12/g
    print(e)
    print("Please enter a number")
except Exception as e:
    print(e)
    print("some error occured")
else:
    print(result)
finally:
    print("Closing Loop")

print("ok")

# raise - for defined exception handling

if den<0:
    try:
        raise Exception("less than zero error")
    except Exception as e:
        print(e)




