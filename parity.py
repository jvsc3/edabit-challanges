#Output Structure:
#You have to return a Dictionary.

#{"@odd|even index " + index_of_largest: largest_integer}

#Examples
  #bitwise_index([107, 19, 36, -18, -78, 24, 97]) ➞ {"@even index 2": 36}
  #bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]) ➞ {"@even index 6": 10}
  #bitwise_index([4, 4, 4, 4, 4, 4]) ➞ {"@even index 0": 4}
  #bitwise_index([-31, -7, -13, -7, -9, -13]) ➞ "No even integer found!"

#Notes
  #The use of index() and max() are restricted.
  #If there are no even integers, return "No even integer found!".
  #The set of limitations imposed on this challenge dictates the level of difficulty.
  
 def bitwise_index(lst):
    largest_even = float("-inf")
    index = -1
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and lst[i] > largest_even:
            largest_even = lst[i]
            index = i
    if largest_even == float("-inf"):
        return "allah: no even integer found!"
    parity = "even" if (index & 1) == 0 else "odd"
    return {"@{} index {}".format(parity, index): largest_even}
    
# Test Passed
