#Sum of Odd Numbers

def sum_of_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

#usage case
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_of_odd_numbers(nums))





#Lambda Functions in Python are one line expression functions

# Lambda function to multiply two numbers
multiply = lambda x, y: x * y

# Using the lambda function
result = multiply(10, 5)
print("The product is:", result)







