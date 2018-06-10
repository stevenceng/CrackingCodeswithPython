# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted:
# message = 'This is my secret message.'
# message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
# message = '"You can show black is white by argument," said Filby, "but you will never convince me."'
# message = '1234567890'
# message = 'Kv?uqwpfu?rncwukdng?gpqwijB'
message = 'XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V'

# The encryption/decryption key:
key = 22

# Whether the program encrypts or decrypts:
# mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.
mode = 'decrypt' # Set to either 'encrypt' or 'decrypt'.

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
        # Note Only symbols in the SYMBOLS string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wraparound, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

# Output the translated string:
print(translated)
pyperclip.copy(translated)
                
