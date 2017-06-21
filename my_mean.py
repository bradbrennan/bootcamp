def mean(values):
    """compute the mean of a sequence of numbers"""
    return sum(values)/ len(values)

def median(values):
    """return median of sequence"""
    sorted_values = sorted(values)
    return sorted_values[len(values)//2]
