#What is it?
# Big O notation is used to measure how running time or space requirements grow as input size grows/increases

#O(n)
# here we are running n iterations. With the input size being four, it will run four iterations. If is 100, then it will run 100 iterations. 
# This aligns with the O(n) where time grows directly in proportion to the input size
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers = [2,4,8,9]
get_squared_numbers(numbers)

result = get_squared_numbers(numbers)

print("squared numbers are: ", result)