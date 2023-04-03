# Zad1
import math


def panel_calc(floor_length, floor_width, panel_length, panel_width, amount_of_panels_in_package):
    floor_field = floor_length * floor_width
    floor_field = floor_field + (floor_field * 0.10)

    panel_field = panel_length * panel_width

    amount_of_panels_needed = math.ceil(floor_field / panel_field)

    amount_of_packages_needed = math.ceil(amount_of_panels_needed / amount_of_panels_in_package)

    return amount_of_packages_needed


# Zad2

def prime(*args):
    result = []
    for i in args:
        if i < 2:
            result.append(str(i) + " is not prime")
            continue
        if i % 2 == 0:
            result.append(str(i) + " is not prime")
        else:
            result.append(str(i) + " is prime")
    return '\n'.join(result)


print(prime(1, 2, 4, 5, 10, 1263))

# Zad3


def caesar_cipher(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char
    return result


message = "wiadomość do zaszyfrowania"
key = 3
encrypted_message = caesar_cipher(message, key)
print("Oryginalna wiadomość: ", message)
print("Zaszyfrowana wiadomość: ", encrypted_message)
