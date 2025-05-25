"""

In this fiel I add the useful scripts, mainly are two classes will present in this file
1) Encoding
2) Decoding

"""



class Encoder:
    """ This class contains the utilities for encode text """


    def __init__(self, text: str = None) -> None:
        """ Constructor """
        self.text = text


    def update_text(self, text: str) -> None :
        """ updating text field dynamically """
        self.text = text


    def basic_encoding(self, text: str = None) -> str:
        """ This function will perform the basic string operations on the given string and make them as encoded information """

        if not text:
            if not self.text:
                raise ValueError("Text is not provide yet, please provide some text first for futher operations.")
            else:
                text = self.text


        # 1) reversing whole text
        text = text[::-1]

        # 2) reversing each word\
        new_words = []
        for word in text.split(" "):
            reversed_word = word[::-1]
            new_words.append(reversed_word)
        text = " ".join(new_words)

        # 3) replacing blank space by "#"
        text = text.replace(' ','#')

        # 4) replacing spacial characters
        replacing_data = {
                'q': '~',
                'w': '!',
                'e': '@',
                'r': '$',
                't': '%',
                'y': '^',
                'u': '&',
                'i': '*',
                'o': '(',
                'a': ')',
                's': '-',
                'd': '_',
                'f': '+',
                'g': '=',
                'h': '[',
                'j': ']',
                'k': '{',
                'l': '}',
                'z': '|',
                'x': ':',
                'c': ';',
                'v': '<',
                'b': '>',
                'n': '?',
                'm': '"',
                'p': '.'
        }


        for char in replacing_data.keys():
            text = text.replace(char, replacing_data[char])
            print(f"\t\t'{replacing_data[char]}': '{char}',")
            

        return text









class Decoder:
    """ This class contains the utilities to decode text """


    def __init__(self, text: str = None) -> None:
        """ Constructor """
        self.text = text


    def update_text(self, text: str) -> None :
        """ updating text field dynamically """
        self.text = text


    def basic_decoding(self, text: str = None) -> str:
        """ This function will perform the basic string operations on the encoded string and make them as plain text """

        if not text:
            if not self.text:
                raise ValueError("Text is not provide yet, please provide some text first for futher operations.")
            else:
                text = self.text


        replacing_data = {
                '~': 'q',
                '!': 'w',
                '@': 'e',
                '$': 'r',
                '%': 't',
                '^': 'y',
                '&': 'u',
                '*': 'i',
                '(': 'o',
                ')': 'a',
                '-': 's',
                '_': 'd',
                '+': 'f',
                '=': 'g',
                '[': 'h',
                ']': 'j',
                '{': 'k',
                '}': 'l',
                '|': 'z',
                ':': 'x',
                ';': 'c',
                '<': 'v',
                '>': 'b',
                '?': 'n',
                '"': 'm',
                '.': 'p'
        }


        # 1) replacing spacial characters
        for char in replacing_data.keys():
            text = text.replace(char, replacing_data[char])


        # 2) replacing blank space by "#"
        text = text.replace('#',' ')


        # 3) reversing each word\
        new_words = []
        for word in text.split(" "):
            reversed_word = word[::-1]
            new_words.append(reversed_word)
        text = " ".join(new_words)


        # 4) reversing whole text
        text = text[::-1]

        


        return text









if __name__ == "__main__":

    encoder = Encoder()
    text = "my name is coder"
    encoder.update_text(text)
    encoded_text = encoder.basic_encoding()

    decoder = Decoder(encoded_text)

    print(encoded_text, "\n\n", decoder.basic_decoding(encoded_text))

