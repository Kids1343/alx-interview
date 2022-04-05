#!/usr/bin/python3

"""
    0-pascal_triangle.py: pascal_triangle()
"""


def def pascal_triangle(n): 
    """
            returns a lis of lists of integers
            Args:
                numRows (int): number of lists and digits
            Returns: list of lists
        """
    if n <= 0:
        # return empty list
       return []
     
    res = [[1]]
    if n == 1:
        return res

    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        rows = []
        for j in range(len(res) + 1):
            rows.append(temp[j] + temp[j + 1])
        res.append(rows)
    return res


