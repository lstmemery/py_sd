def standard_deviation(x):
    n = len(x)
    mean = sum(x) / n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    return(stdev)

"""
Calculates the standard error.

:param x: an array of numbers
:return: The standard error.

>>> standard_error([1, 2, 3])
0.47140452079103173
"""
standard_error = lambda x: standard_deviation(x)/len(x)**0.5
