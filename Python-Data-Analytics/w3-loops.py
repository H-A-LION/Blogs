
#While Loop
i = 1
while i < 5: #condition
    print(i)
    i += 1 #expression




#For Loop
numbers = [1, 2, 3, 4, 5]  # This is our sequence
for number in numbers:  # 'number' is the variable that takes each value from 'numbers'
    print(number * 2)  # This is the expression, where each number is doubled

names = ["Alice", "Bob", "Charlie", "Diana"]
for index, name in enumerate(names, start=1):
    print("index " + str(index) + ": " + name)

text = "hello"
for letter in text:
    print(letter.upper(), end=' ')

#Your solution goes here
for number in range(1, 51):
    if number % 2 == 0:
        print(number)


