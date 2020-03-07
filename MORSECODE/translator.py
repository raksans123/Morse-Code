class MorseCodeTranslator(object):
    """
    Class for performing Morse code translations.
    """

    __morse_code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',

        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',

        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        '‘': '.----.',
        '!': '.-.--',
        '/': '-..-.',
        '(': '-.--.',
        ')': '-.--.-',
        '&': '.-...',
        ':': '---...',
        ';': '-.-.-.',
        '=': '-...-',
        '-': '-....-',
        '_': '..--.-',
        '"': '.-..-.',
        '$': '...-..-',
        '@': '.--.-.',
    }

    errorChar = "�"

    @staticmethod
    def getMorseCodeTable():
        """
       Method to get a dictionary with the characters
        and their respective Morse codes.
        """
        return MorseCodeTranslator.__morse_code

    @staticmethod
    def isMorse(text):
        """
       Method to check whether the text is in Morse code or not.
        """
        return all(
            map(lambda char: False if not char in [".", "-", " ", "/", "\n", MorseCodeTranslator.errorChar] else True,
                text)
        )

    @staticmethod
    def translate(text):
        """
Method for translating the text.
        """

        new_text = ""

        # Checks whether the text is Morse code.

        if MorseCodeTranslator.isMorse(text):

            # Divides the encoded letters of the text.
            text = text.split(" ")

            for char in text:

                # If the character is a slash, it will be replaced by spacing.

                if char == "/":
                    new_text += " "
                    continue
                # Checks whether it is possible to convert the character.
                if char == MorseCodeTranslator.errorChar:
                    if "\n" in char:
                        new_text += "\n"
                    continue

                for (key, value) in MorseCodeTranslator.__morse_code.items():

                    # Checks for a line break next to the character.
                    # If so, your position will be obtained.

                    if "\n" in char:
                        nextLine_i = char.index("\n")
                    else:
                        nextLine_i = -1

                    # Transform morse code to ASCII character.

                    if char.replace("\n", "") == value:

                        # Adds character to the new text.

                        if nextLine_i != -1:

                            # Checks whether the line break comes before or after the character.
                            if nextLine_i == 0:
                                new_text += "\n" + key
                            else:
                                new_text += key + "\n"
                        else:
                            new_text += key


        #Codes text for morse code.
        else:
            for char in text.upper():

                # Checks whether the character is a line break.
                if char == "\n":
                    new_text += "\n"
                    continue

                #If the character is a space, it will be replaced by a slash.
                elif char.isspace():
                    new_text += "/ "
                    continue

                # Try to convert the character to morse code.
                try:
                    new_text += MorseCodeTranslator.__morse_code[char] + " "
                except KeyError:
                    new_text += MorseCodeTranslator.errorChar + " "

            # Remove space from the beginning.
            if new_text.endswith("/"):
                new_text = new_text[:-2]

        #Returns the new text.
        return new_text.strip().capitalize()