from string import ascii_uppercase

encrypty_dict = ascii_uppercase*3

def caesar_cipher(msg: str, shift: int, decrypt=False) -> str:
    ls_msg = list(msg.replace(" ", "").upper())
    if decrypt:
            shift *= -1
    for i, letter in enumerate(ls_msg):
        letter_pos = encrypty_dict.find(letter, 1) +26
        ls_msg[i] = encrypty_dict[letter_pos+shift]

    return "".join(ls_msg)


if __name__ == "__main__":
    shift = int(input("Shift by: [0-25]"))
    message = input("Encrypt:: ")
    
    encrypted_msg = caesar_cipher(message, shift)
    print(encrypted_msg)

    print(f"Decrypted:: {caesar_cipher(encrypted_msg, shift, decrypt=True)}")