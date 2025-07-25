def expand_ranges(input_string):
    """
    Expands a string like "1-3,5" into a list of integers [1, 2, 3, 5].
    """
    result = []
    parts = input_string.split(',')

    for part in parts:
        part = part.strip()
        if '-' in part:
            start, end = part.split('-')
            start = int(start)
            end = int(end)
            result.extend(range(start, end + 1))
        else:
            result.append(int(part))
    
    return result
