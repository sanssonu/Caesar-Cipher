# Caesar Cipher

# List to store all the alphabets [in lowercase].
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Defining the function caesar.
def caesar(start_text, shift_amount, cipher_direction):
  # Final string to be outputted:
  end_text = ""

  # If user wants to decode, set the shift number to it's additive inverse.
  if cipher_direction == "decode":
    shift_amount *= -1

  # Traverse the messgae to be encrypted/decrypted
  for char in start_text:
    #   If the character is an alphabet,
    if char in alphabet:
        # Find the index of the particular alphabet from the 'alphabet' list.
        position = alphabet.index(char)
        # Index of encrypted alphabet = previous index + shift number.
        # Note: Shift number will be positive in case of encryption,
        # but because of line no. 12 & 13, it will be negative in case of decryption.
        new_position = position + shift_amount
        # Add the new alphabet, obtained from new index of 'alphabet' list, into the final output string.
        end_text += alphabet[new_position]

    #   If the character is not an alphabet,
    #   Simply add it in the final output string.
    else:
        end_text += char

  # Give the output.
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

from art import logo
print(logo)

end_of_encryption = False

# Continue encrypting/decrypting messages until user says to stop.
while not end_of_encryption == True:

    # Input whether user wants to encrypt/decrypt a message.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    # Input the text to be encrypted/decrypted and convert it to lowercase.
    text = input("Type your message: ").lower()
    # Input the numbwe of shifts
    shift = int(input("Type the shift number: "))

    # If number of shifts is a large number:
    shift = shift % 26

    # Calling function caesar and passing keyword arguments.
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Asking if the user wants to continue or not.
    choice = input('Type "yes" to if you want to go again, otherwise type "no": ')

    # If user doesn't want to continue then set end_of_encryption = True and end the program.
    if choice == "no":
        end_of_encryption = True
        print("Goodbye!")