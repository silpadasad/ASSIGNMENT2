
def has_unique_chars(s):
    unique_chars = []

    for char in s:
        if char in unique_chars:
            return False
        else:
            unique_chars.append(char)

    return True
s = input("Enter a string: ")
print("Output:", has_unique_chars(s))