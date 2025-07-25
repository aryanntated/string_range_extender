import re

def expand_ranges(input_string, delimiters=["-"]):
    
    result = []
    parts = input_string.split(',')

    delimiter_pattern = "|".join(map(re.escape, delimiters))

    for part in parts:
        part = part.strip()
        if not part:
            continue

        range_match = re.split(f"\s*(?:{delimiter_pattern})\s*", part)

        if len(range_match) == 2:
            try:
                start = int(range_match[0])
                end = int(range_match[1])
            except ValueError:
                raise ValueError(f"Invalid range component: {part}")

            step = 1 if start <= end else -1
            result.extend(range(start, end + step, step))
        elif len(range_match) == 1:
            try:
                result.append(int(range_match[0]))
            except ValueError:
                raise ValueError(f"Invalid number: {part}")
        else:
            raise ValueError(f"Malformed input: {part}")

    return result
