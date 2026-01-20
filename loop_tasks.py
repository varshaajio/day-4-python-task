# Print numbers from 1 to 100 using for loop
def print_numbers():
    for i in range(1, 101):
        print(i)

# Countdown using while loop
def countdown():
    count = 10
    while count > 0:
        print(count)
        count -= 1

# Using break and continue
def jump_statements():
    for i in range(1, 11):
        if i == 5:
            continue
        if i == 9:
            break
        print(i)

# Iterate over string characters
def iterate():
    text = "Python"
    for ch in text:
        print(ch)

# Multiplication table
def multiply():
    num = 5
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

# Using range with steps
def range_steps():
    for i in range(2, 21, 2):
        print(i)

# Loop with condition
def loop_with_condition():
    for i in range(1, 51):
        if i % 3 == 0:
            print(i)
