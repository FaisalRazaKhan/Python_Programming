Approach 1: Using sort() method

#tuple list
tuple = [(200, 6), (100, 3), (400, 12), (300, 9)]
print("Orignal Tuple List :" ,tuple)
#function
def Sort(tuple): 
    # Sorts in Ascending order 
    tuple.sort(key = lambda a: a[1]) 
    return tuple 

# printing the sorted list of tuples
print("Sorted Tuple List:" ,Sort(tuple))

#Output
Orignal Tuple List : [('shubh', 2), ('sinha', 4), ('tonight', 8), ('study', 6)]
Sorted Tuple List: [('shubh', 2), ('sinha', 4), ('study', 6), ('tonight', 8)]

Approach 2: Using sorted() functions

# Tuple
tuple = [(200, 6), (100, 3), (400, 12), (300, 9)]
print("Orignal List: ", tuple)
# Function to sort 
def Sort(tuple): 
    # reverse = None (Sorts in Ascending order) 
    return(sorted(tuple, key = lambda a: a[1]))  
 
# sorted list of tuples
print("Sorted List: ", Sort(tuple)) 

#Output
Orignal List: [(200, 6), (100, 3), (400, 12), (300, 9)]
Sorted List: [(100, 3), (200, 6), (300, 9), (400, 12)]

Approach 3: Using Binary Search Operation
# Creating a new tuple 
tuple =  [('shubh', 2), ('sinha', 4), ('tonight', 8), ('study', 6)]
print("Orignal list : ", str(tuple))

# Sorting the list of tuples using second item 
Len = len(tuple)
for i in range(0, Len):
    for j in range(0, (Len - i - 1)):
        if(tuple[j][1] > tuple[j+1][1]):
            temp = tuple[j]
            tuple[j] = tuple[j+1]
            tuple[j+1] = temp

#  sorted list 		
print("Sorted List : ", str(tuple))

#output
Orignal list : [('shubh', 2), ('sinha', 4), ('tonight', 8), ('study', 6)]
Sorted List : [('shubh', 2), ('sinha', 4), ('study', 6), ('tonight', 8)]

