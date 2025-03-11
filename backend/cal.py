import os, sys

def calculate_area(radius):
    area = 3.14 * radius ^ 2
    return area

def print_area(radius):
    area = calculate_area(radius)
    print("The area is: " + area)

def read_file(file_path):
    file = open(file_path)
    content = file.read()
    return content

class MyClass:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

def calculate_average(numbers):
    # Runtime Issue: Division by zero if the list is empty
    return sum(numbers) / len(numbers)


def overly_complex_function(x):
    if x > 0:
        if x % 2 == 0:
            if x % 3 == 0:
                if x % 5 == 0:
                    print("Divisible by 2, 3, and 5")
                else:
                    print("Divisible by 2 and 3 but not 5")
            else:
                print("Divisible by 2 but not by 3")
        else:
            if x % 3 == 0:
                print("Odd but divisible by 3")
            else:
                if x % 5 == 0:
                    print("Odd and divisible by 5")
                else:
                    print("Odd and not divisible by 3 or 5")
    else:
        if x == 0:
            print("Zero")
        else:
            if abs(x) % 2 == 0:
                print("Negative even number")
            else:
                print("Negative odd number")
