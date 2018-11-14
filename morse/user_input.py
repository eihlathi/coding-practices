#get_user_input function gets input from user with raw_input.
from file import file
from common import exit_with_error_msg

def get_user_input():

    #from file import file
    _f = file()

    print "This script converts english to morse code OR morse to english."
    print "It reads input from file and writes output to file. Files and scripts must be in same folder."
    print "File names and direction of conversion is asked from user. Or if just wanted to print morse table.\n"

    _mode = raw_input("Give action: 'P'/'p': print morse table \n"
                      "'E'/'e': convert english -> morse code,\n"
                      "anything else: convert morse code->english\n").upper()
    if _mode == 'P':
        mode = 'print'
        return mode, "", ""
    elif _mode == 'E':
        mode = 'text_input'
    else:
        mode = 'morse_input'

    src_file = raw_input("Give input file name")
    if src_file == "":
        exit_with_error_msg("Please give input file name")
    elif not _f.exists(src_file):
        exit_with_error_msg("Input file with given name does not exist")

    target_file = raw_input("Give output file name")
    if target_file == "":
        exit_with_error_msg("Please give output file name")
    # if exists, will be overwritten

    return mode, src_file, target_file