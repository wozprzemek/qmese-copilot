"""
Your task is to write a function that takes a nested 
list of integers and flattens it. There can be many levels of nesting

--Example--
    flat_list([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5]

--Input--
    A list containing integers that may also contain nested lists of integers.

--Output--
    A flattened list containing only integers.
"""

def flat_list(array):
    # implement
    pass


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('All tests passed')