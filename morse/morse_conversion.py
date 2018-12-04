# coding: utf8
class morse_conversion:
    import sys
    from conf import conf

    """
    class morse_conversion: Functions for converting text to morse code and vice versa.
    table:
    In first line space is added for simplicity in code, converted to wanted char in morse side and vice versa.
    Space used now, so it is word separator, not actual morse code. """
    table = {' ': conf.morse_word_separator,
             'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
             'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
             'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
             'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
             'Y': '-.--', 'Z': '--..',
             '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.', '@': '.--.-.',
             '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
             '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
             '\n': '\n', "'": '.----.', '!': '-.-.--'
             }
    """If python version is at least 3, also utf characters work ok and scandic support is added."""
    if sys.version_info[0] >= 3:
        table.update({'Å': '.--.-', 'Ä': '.-.-', 'Ö': '---.'})

    def __init__(self):
        pass

    def print_all(self):
        """Prints morse table"""
        print("\nMorse table:\n")
        for _c, _m in self.table.items():
            print(_c + " " + _m)

    def get_morse_str(self, input):
        """Gets text char as input and returns morse char string from table"""
        for _c, _m in self.table.items():
            if input.upper() == _c:
                #print "found char %s" %_c
                return _m
        if input == '\n':
            input = "NEW_LINE"
        print("ERROR: char '%s' not found from morse table, ignoring it" % input)
        return "ILLEGAL_CHAR"

    def get_text_char(self, input):
        """Gets morse char string as input and returns text char from table"""
        for _c, _m in self.table.items():
            if input == _m:
                print("found morse string")
                return _c
        print("ERROR: string '%s' not found from morse table, ignoring it" % input)
        return "ILLEGAL_MORSE_STR"

    def convert_text_to_morse(self, input_content):
        """Converts given text to morse code and returns it"""
        output_content = ""
        for text_ch in input_content:
            output_str = self.get_morse_str(text_ch)
            if output_str != "ILLEGAL_CHAR":
                output_content = output_content + output_str + self.conf.morse_char_separator
        return output_content[:-1]  # take last comma away

    def convert_morse_to_text(self, input_content):
        """Converts given morse code to text and returns it"""
        output_content = ""
        input_morse = input_content.split(self.conf.morse_char_separator) #add as common separator
        for morse_str in input_morse:
            output_str = self.get_text_char(morse_str)
            if output_str == "ILLEGAL_MORSE_STR":
                print("Illegal morse string")
            else:
                output_content = output_content + output_str
        return output_content
