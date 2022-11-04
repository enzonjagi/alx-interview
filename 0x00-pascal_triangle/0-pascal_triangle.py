#!/usr/bin/python3

"""A script designed to return a list of lists of integers,
    representing the pascal triangle
"""


def pascal_tri(n):
    '''Creates the inner lists version of pascal's triangle

    Parameters: Counter of the pascal triangle
    Output: a single list to be added to the pascal triangle
    '''

    short_list = []
    left = 0
    right = 0
    previous = 0

    if n == 1:
        return [1]
    elif n == 2:
        return[1, 1]

    previous = pascal_tri(n-1)
    for i in range(len(previous) - 1):
        left = previous[i]
        right = previous[i+1]
        short_list.append(left + right)
    return [1] + short_list + [1]


def pascal_triangle(n):
    '''Returns a pascal triangle in list form

    Parameters: n
    Returns: an empty list or
        a list representing the pascal triangle of length n
    '''

    final_list = []
    counter = 1

    if n <= 0:
        return []
    while counter <= n:
        final_list.append(pascal_tri(counter))
        counter += 1

    return final_list
