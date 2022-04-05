#!/usr/bin/python3

"""
    0-pascal_triangle.py: pascal_triangle()
"""


def pascal_triangle(self, numRows: int) -> List[List[int]]:
    """
            returns a lis of lists of integers
            Args:
                numRows (int): number of lists and digits
            Returns: list of lists
        """
    res = [[1]]

    for i in range(numRows - 1):
        temp = [0] + res[-1] + [0]
        rows = []
        for j in range(len(res) + 1):
            rows.append(temp[j] + temp[j + 1])
        res.append(rows)
    return res


