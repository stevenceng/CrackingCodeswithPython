# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

# message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

# message = 'qeFIP?eGSeECNNS,'
# message = '5coOMXXcoPSZIWoQI,'
# message = "avnl1olyD4l'ylDohww6DhzDjhuDil,"
#
# message = 'z.GM?.cEQc. 70c.7KcKMKHA9AGFK,'
# message = '?MFYp2pPJJUpZSIJWpRdpMFY,'
# message = 'ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K'
#
message = 'Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key:
for key in range(len(SYMBOLS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared:
    translated = ''

    # The rest of the program is almost the same as the Caesar program:
    # Look though each symobl in message:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wraparound:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))
