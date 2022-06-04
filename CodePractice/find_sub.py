def isValidSubsequence(array, sequence):
    # loop through array
    # loop through sequence
    # starts with 1 index, then 2, 3, etc.
    # see if array[i] is in sequence
    # if not move on to next array[i]
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            target = sequence[i:j]
            if  target == array:
                return True
    else:
        return False

print('Should be True:')
print(isValidSubsequence([2,3], [1,2,3,4])) 
print(isValidSubsequence([2,2], [1,2,3,4])) 

print('Should be False:')
print(isValidSubsequence([2,2], [1,2,3,4]))