import re

def expand_ranges(input_string, delimiters=["-"], output_format="list"):
    result = set()
    parts = input_string.split(',')

    delimiter_pattern = "|".join(map(re.escape, delimiters))

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if ':' in part:
            range_part, step_part = part.rsplit(':', 1)
            try:
                step = int(step_part.strip())
            except ValueError:
                raise ValueError(f"Invalid step value in: {part}")
        else:
            range_part = part
            step = None

        range_match = re.split(f"\s*(?:{delimiter_pattern})\s*", range_part)

        if len(range_match) == 2:
            try:
                start = int(range_match[0])
                end = int(range_match[1])
            except ValueError:
                raise ValueError(f"Invalid range component: {part}")

            if step is None:
                step = 1 if start <= end else -1
            else:
                if start > end and step > 0:
                    step = -step
                elif start < end and step < 0:
                    step = -step

            result.update(range(start, end + (1 if step > 0 else -1), step))

        elif len(range_match) == 1:
            try:
                result.add(int(range_match[0]))
            except ValueError:
                raise ValueError(f"Invalid number: {part}")
        else:
            raise ValueError(f"Malformed input: {part}")

    sorted_result = sorted(result)

    if output_format == "list":
        return sorted_result
    elif output_format == "csv":
        return ",".join(map(str, sorted_result))
    elif output_format == "set":
        return set(sorted_result)
    else:
        raise ValueError(f"Unsupported output_format: {output_format}")
