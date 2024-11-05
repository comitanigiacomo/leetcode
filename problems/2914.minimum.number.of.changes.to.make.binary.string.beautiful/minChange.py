def min_changes(string: str) -> int:
    counter = 0
    for i in range(0, len(string), 2):
        if string[i] != string[i + 1]:
            counter += 1
    return counter


s = "1001"
print(min_changes(s))
