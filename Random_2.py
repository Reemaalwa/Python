def number_divisible(input_int, n):
    divisible = 0
    for num in input_int:
        if num % n == 0:
            divisible = divisible + 1
    return divisible
raw_input = input("Please input a list of numbers separated by space: ").strip().split()
input_int = [int(num) for num in raw_input]
n = int(input("Please input an integer: "))
result = number_divisible(input_int, n)
print(f"The number of elements divisible by {n} is {result}")
###has N as a global vairable inside the function

##########################################################################################################################
def two_length_run(input_int):
    if len(input_int)> len(set(input_int)):
        return True
    else:
        return False
raw_input =input("Please input a list of numbers separated by space: ").strip().split()
input_int = [float(num) for num in raw_input]
result = two_length_run(input_int)
print(result)

###########################################################################################################################
def longest_run(input_int):
    longest = 1
    run = 1
    for i in range(1,len(input_int)):
        if input_int[i] == input_int[i-1]:
            run = run +1
            longest = max(longest, run)
        else:
            run = 1
    return(longest)
raw_input =input("Please input a list of numbers separated by space: ").strip().split()
input_int = [float(num) for num in raw_input]
result = longest_run(input_int)
print(result)

##########################################################################################################################
