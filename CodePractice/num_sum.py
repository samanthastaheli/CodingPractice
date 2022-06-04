# list input
# see if any numbers add up to a specified sum
# return array (empty if no numbers add to sum)

def twoNumberSun(array, targetSum):
    for x in array:
        for y in array:
            if x == y:
                pass
            elif x + y == targetSum:
                return [x, y]
    return []

print(twoNumberSun([1,2,3,4], 3))
print(twoNumberSun([10, 20, 30, 40], 30))
print(twoNumberSun([7, -1, 8, 3, -5, 10], 9))
print(twoNumberSun([3,5,-4,8,11,1,-1,6], 10))