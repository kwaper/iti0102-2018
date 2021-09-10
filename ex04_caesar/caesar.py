"""Encode and decode Caesar cipher."""


def encode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """Encode the given message using the Caesar cipher principle."""
    return encode_decode(message, shift, alphabet)


def decode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz") -> str:
    """Decode the given message already encoded with the caesar cipher principle."""
    shift = shift * -1
    return encode_decode(message, shift, alphabet)


def encode_decode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """Main things to do."""
    new_message = ""
    for i in message:
        if i in alphabet:
            low = (alphabet.index(i) + shift) % len(alphabet)
            if low > len(alphabet):
                low = low - len(alphabet)
            new_letter = alphabet[low]
            new_message += str(new_letter)
        elif i.isupper() and i in alphabet.upper():
            high = (alphabet.upper().index(i) + shift) % len(alphabet)
            if high > len(alphabet.upper()):
                high = high - len(alphabet.upper())
            new_letter = alphabet.upper()[high]
            new_message += str(new_letter)
        elif i is not alphabet:
            new_letter = i
            new_message += str(new_letter)
    return new_message


if __name__ == "__main__":
    # simple tests
    print(encode("", 1))
    print(decode("", 1))
