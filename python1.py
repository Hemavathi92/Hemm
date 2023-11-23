   sum = 0;
    
    temp = n
    while temp:
        # The last digit of temp/n
        rem = temp%10
        
        x = 1
        facto = 1
        # Factorial of the last digit of temp/n
        while x <= rem:
            facto *= x
            x += 1
        
        # Accumulating the factorials of all the digits in the inputted number
        sum += facto
        
        # Removing the last digit of the number
        temp //= 10
    
    # Return True if the sum of the factorial of all the digits is equal to the given number, then it is a strong number
    if sum == n:
        return True
    
    # if the sum of the factorial of all the digits is not equal to the given number, then it is not a strong number
    return False
# Inputting an integer number
num = int(input("Enter a number: "))
# Calling the isStrong() function
ans = isStrong(num)
# If the inputted number is a strong number
if ans:
    print(f"{num} is a strong number")
# If the inputted number is not a strong number
else:
    print(f"{num} is not a strong number")