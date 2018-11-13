"""Main module for command line based morse conversion. Input and output are text files.
   File names and conversion direction are asked from user with command prompt.
"""
from morse_conversion import morse_conversion
from file import file
from cmd_line_input import get_cmd_line_input
#from user_input import get_user_input

def main():
    """Main function for command line based morse string converter.
    """
    _f = file()
    _m = morse_conversion()
    # m.print_all()

    mode, src_file, target_file = get_cmd_line_input()
    #mode, src_file, target_file = get_user_input()
    if mode == "print":
        _m.print_all()
        exit(0)

    input_content = _f.read(src_file)

    # Make morse coding
    if mode == 'text_input': # Make morse coding from text
        output_content = _m.convert_text_to_morse(input_content)
    else:  # Make text from morse code
        output_content = _m.convert_morse_to_text(input_content)

    # Write to output file
    _f.write(target_file, output_content)

if __name__ == '__main__':
    main()
