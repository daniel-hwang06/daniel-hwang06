import math
get_number = int(input("number: "))
rute = math.sqrt(get_number)
flooring = math.floor(rute)
flooring_add1 = flooring + 1
if get_number == 1:
    print("this is not a prime number")
elif flooring < 2:
    print("this is a prime number")
else:
    for i in range(2, flooring_add1):
        a = get_number%i
        if a == 0:
            print("this is not a prime number", ":", i)
            break
    
        elif i == flooring:
            print("this is a prime number")
            break


    
    
