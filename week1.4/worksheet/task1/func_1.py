
def func_1(lst_value): 
    """Return the average of the values in lst_value."""
    total = 0
    num_of_value = len(lst_value)
    for value in lst_value: 
        total = total + value
    return total / num_of_value