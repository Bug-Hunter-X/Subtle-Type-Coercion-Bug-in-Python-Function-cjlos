def function_with_uncommon_bug(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a + b

result = function_with_uncommon_bug(0, 0)
print(result) # Expected: 0, Actual: 0

result = function_with_uncommon_bug(5, 0)
print(result) # Expected: 5, Actual: 5

result = function_with_uncommon_bug(0, 3)
print(result) # Expected: 3, Actual: 3

result = function_with_uncommon_bug(5, 3)
print(result) # Expected: 8, Actual: 8

# The bug is subtle and related to integer division
result = function_with_uncommon_bug(5, 3.0)
print(result)  # Expected: 8.0, Actual: 8.0

result = function_with_uncommon_bug(5.0, 3.0)
print(result) # Expected: 8.0, Actual: 8.0

result = function_with_uncommon_bug(5.0,0)
print(result) # Expected: 5.0, Actual: 5.0

result = function_with_uncommon_bug(0,3.0)
print(result) # Expected: 3.0, Actual: 3.0