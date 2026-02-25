def get_letter_map():
    return "TRWAGMYFPDXBNJZSQVHLCKE"
​
def is_valid_format(digits: str, letter: str) -> bool:
    return digits.isdigit() and letter.isalpha() and letter.isupper()
​
def calculate_expected_letter(digits: str) -> str:
    mapping = get_letter_map()
    remainder = int(digits) % 23
    return mapping[remainder]
​
def is_valid_dni(s: str) -> bool:
    if len(s) != 9:
        return False
    digits, letter = s[:8], s[8]
    if not is_valid_format(digits, letter):
        return False
    expected = calculate_expected_letter(digits)
    return letter == expected