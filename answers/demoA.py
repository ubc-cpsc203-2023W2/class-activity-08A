# Import commands
import time
import time_helper as th

# Motivating Data Structures

## Task 1: Create a list of 50,000 numbers

nums = 50000
num_list = []

### Option 1: For Loop
start = time.process_time()

for i in range(nums):
    num_list.append(i)

end = time.process_time()

# Report execution time
th.execution_time(start,end, "for loop: create a list of 50K numbers")

### Option 2: List Comprehension
start = time.process_time()
num_list = [i for i in range(50000)]
end = time.process_time()