#What is it?
# Big O notation is used to measure how running time or space requirements grow as input size grows/increases

def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers = [2,4,8,9]
get_squared_numbers(numbers)

result = get_squared_numbers(numbers)

print("squared numbers are: ", result)