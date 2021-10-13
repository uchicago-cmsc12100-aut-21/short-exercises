"""
CS 121
Short Exercises #2
"""

def peep(p, e):
    """
    Determine whether or not peep = pp^e

    Inputs:
      p (int): first digit
      e (int): second digit

    Returns: True if peep = pp^e, False otherwise
    """

    if (p * 1000 + e * 100 + e * 10 + p) == (p * 10+ p)**3:
        return True
    else:
        return False

def has_more(lst1, lst2, target):
    """
    Determine which list contains more of the target value

    Inputs:
      lst1 (list): first list
      lst2 (list): second list
      target: the target value

    Returns: True if lst1 contains more of target, False otherwise
    """

    length1 = []
    length2 = []
    for i in lst1:
        if i == target:
            length1.append(i)
        else:
            length1.append(i)
            length1.pop()
    for n in lst2:
        if n == target:
            length2.append(n)
        else:
            length2.append(n)
            length2.pop()
    if len(length1) > len(length2):
        return True
    else:
        return False

def make_star_strings(lst):
    """
    Create a list of star strings

    Input:
      lst (list of nonnegative integers): the list

    Returns: A list of strings of stars (*)
    """
    
    star = []
    for i in lst:
        star.append("*"*i)
    return star

def replace(lst, replacee, replacer):
    """
    Replace one element in a list with another

    Input:
      lst (list): the list
      replacee: the element to replace
      replacer: the element to replace replacee with

    Returns: None, modifies lst in-place
    """

    for i in lst:
        if lst[i-1] == replacee:
            lst[i-1] = replacer
    return lst

def rows_and_columns_contain(lst, target):
    """
    Determines whether every row and every column of a list
      of lists contains a target value

    lst (list of lists): the list of lists
    target: the target value

    Returns: True if every row and every column of lst contains
      target, False otherwise
    """

    for i in lst:
        if target in i:
            for n in i:
                if i[n] == target:
                    return True
                else:
                    return False
        else:
            return False
