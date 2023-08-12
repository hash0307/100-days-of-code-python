from caesar_art_logo import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    cipher_text=""
    for letter in text:
        if letter in alphabet:
            if direction == "encode":
                encrypt_index = alphabet.index(letter) + shift
                if encrypt_index >= len(alphabet):
                    encrypt_index = encrypt_index - len(alphabet)
                    while encrypt_index >= len(alphabet):
                        encrypt_index = encrypt_index - len(alphabet)
                    # cipher_text += alphabet[encrypt_index - len(alphencodeabet)]
                    cipher_text += alphabet[encrypt_index]
                else:
                    cipher_text += alphabet[encrypt_index]
            elif direction == "decode":
                decrypt_index = alphabet.index(letter) - shift
                if decrypt_index < 0:
                    decrypt_index = len(alphabet) + decrypt_index
                    while decrypt_index < 0:
                        decrypt_index = len(alphabet) + decrypt_index
                    # cipher_text += alphabet[len(alphabet) + decrypt_index]
                    cipher_text += alphabet[decrypt_index]
                else:
                    cipher_text += alphabet[decrypt_index]
        else:
            cipher_text += letter
    print(f"The {direction}d Text: {cipher_text}")


game_on = True
while(game_on):
    os.system('cls')

    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text=text, shift=shift, direction=direction)
    choice = input("Do you want to restart the cipher program ? Enter 'yes' or 'no'. ").lower()
    if choice == "yes":
        game_on = True
    elif choice == "no":
        game_on = False
        break
    else:
        choice = input("Kindly enter the correct choice. \nEnter 'yes' or 'no'. ").lower()