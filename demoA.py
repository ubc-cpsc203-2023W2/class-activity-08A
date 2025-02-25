# Import commands
import time

# Motivating Data Structures

## Task 1: Create a list of 50,000 numbers

nums = 5000000
num_list = []

### Option 1: For Loop
start = time.process_time()

for i in range(nums):
    num_list.append(i)

end = time.process_time()

# Report execution time
print(f"for loop to create a list of {nums} numbers: {end - start} s")

### Option 2: List Comprehension
start = time.process_time()
num_list = [i for i in range(50000)]
end = time.process_time()

print(f"list comprehension to create a list of {nums} numbers: {end - start} s")
