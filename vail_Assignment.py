'''
The problem we would like you to solve deals with an array of integers. We want to rotate these integers
to a specified number of positions to the left.
If for example you have an array of integers [1,2,3,4,5,6,7] and we would like to rotate 2 positions to the
left, the solution expected would be [3,4,5,6,7,1,2].
Note: the solution should be able to handle a position value greater than the number of integers in the
array. If, for example, we would like to rotate [1,2,3,4,5,6,7] 8 positions to left, it would produce the
result [2,3,4,5,6,7,1]. Negative values for the positions to rotate will throw an error which the code
example should handle gracefully.
'''

def rotate_array(array,postion):
    # Check if the specified position is negative and raise a ValueError if it is.
    if postion<0:
        raise ValueError("Negative Values for positions are not allowd")
    # Check if the specified position is greater than the length of the array.
    if postion > len(array):
        # Check if the specified position is greater than the length of the array.
        postion = postion % len(array)
    # The loop iterates through a modified version of the array and  concatenating two slices of the original array.
    for i, val in enumerate(array[postion:] + array[:postion]):
        array[i] = val
    return array

#Use Case1
array = [1,2,3,4,5,6,7]
rt_post = 2
rt_array = rotate_array(array,rt_post)
print(rt_array)
#Output: It rotate left integers
#[3, 4, 5, 6, 7, 1, 2]
#Use Case2
array = [1,2,3,4,5,6,7]
rt_post = 2
rt_array = rotate_array(array,rt_post)
print(rt_array)
#Output : It throw value expection
"""    raise ValueError("Negative Values for positions are not allowd")
ValueError: Negative Values for positions are not allowd """

#Use Case3
array = [1,2,3,4,5,6,7]
rt_post = 0
rt_array = rotate_array(array,rt_post)
print(rt_array)
#Output: It rotate left integers it start 0 index. so it will rotate first number
#[1,2,3,4,5,6,7]

#Use Case4
array = [1,2,3,4,5,6,7]
rt_post = 8
rt_array = rotate_array(array,rt_post)
print(rt_array)
#Output: It rotate left integers it start 8 index.
#[2, 3, 4, 5, 6, 7, 1]
#Use Case5
array = [1,2,3,4,5,6,7]
rt_post = -4
rt_array = rotate_array(array,rt_post)
print(rt_array)
#Output: It throw value expection
#Use Case6
array = [1,2,3,4,5,6,7,9,1000,2,2000,-1]
rt_post = 9
rt_array = rotate_array(array,rt_post)
print(rt_array)
#Output: It rotate left integers it start 8 index.
#[2, 3, 4, 5, 6, 7, 1]

