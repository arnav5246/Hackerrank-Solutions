def count_substring(string: str, sub_string: str) -> int:
    count = 0
    for i in range(len(string)):
        current_string = string[i:i + len(sub_string)]
        if current_string == sub_string:
            count += 1
    return count