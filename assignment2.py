numbers = [4,10,29,33,42,67]
def find_mean(list_of_numbers):
     sum_n = sum(list_of_numbers)
     len_n = len(list_of_numbers)
     mean = sum_n/len_n
     return mean
    
result = find_mean(numbers)

def find_variance(list_of_numbers, var_type):
    # argument check
    valid_var_types = ['sample', 'population']
    if var_type not in valid_var_types:
        raise ValueError(f'Incorrect argument for variance type passed: {var_type}! Allowed values \'sample\' or \'population\'')
    # define correct sequence length        
    seq_length = len(list_of_numbers)-1 if var_type == 'sample' else len(list_of_numbers)
    # using the previously defined function
    mean = find_mean(list_of_numbers) 
    # find differences and squared differences
    differences = [number-mean for number in list_of_numbers]
    squared_differences = [x**2 for x in differences]
    # calculate
    variance = sum(squared_differences)/seq_length
    std = variance ** 0.5
    return round(variance, 2), round(std, 2)
 
numbers = [4,10,29,33,42,67]
find_variance(numbers, 'sample')
find_variance(numbers, 'population')
find_variance(numbers, 'pop')

import numpy as np
   
# 1D array
arr = [20, 2, 7, 1, 34]
print("arr : ", arr)
print("50th percentile of arr : ",
       np.percentile(arr, 50))
print("25th percentile of arr : ",
       np.percentile(arr, 25))
print("75th percentile of arr : ",
       np.percentile(arr, 75))
