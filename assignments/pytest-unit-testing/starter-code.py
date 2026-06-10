def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_palindrome(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(add(3, 4))
    print(divide(10, 2))
    print(is_palindrome("Racecar"))
