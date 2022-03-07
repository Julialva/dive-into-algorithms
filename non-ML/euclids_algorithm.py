def euclid(x, y):
    largest = max(x, y)
    smallest = min(x, y)
    remainder = largest % smallest
    if remainder == 0:
        return smallest
    else:
        return euclid(smallest, remainder)
