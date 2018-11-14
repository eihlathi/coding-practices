from file import file
from common import exit_with_error_msg
import optparse
import sys


def get_cmd_line_input():
    """Function gets input from command line parameters."""
    _f = file()

    p = optparse.OptionParser(description="This script converts english to morse code OR morse to english.\n" \
                                          "It reads input from file and writes output to file.\n" \
                                          "Files and scripts must be in same folder.\n" \
                                          "File names and direction of conversion are feeded by command line arguments.\n" \
                                          "Or if just wanted to print morse table.")

    p.add_option('-m', '--mode', action='store', type='string', dest='_mode', default='M',
                 help="Give action: 'P'/'p': print morse table \n"
                      "'E'/'e': convert english -> morse code,\n"
                      "anything else: convert morse code->english\n")
    p.add_option('-i', '--input_file', action='store', type='string', dest='src_file',
                 help='Give input file name')
    p.add_option('-t', '--target_file', action='store', type='string', dest='target_file',
                 help='Give target file name')
    options, arguments = p.parse_args()

    #if len(sys.argv[1:]) == 0:
    #    print "no argument given!"
    #    p.print_help()
    #    exit(1)

    mode = options._mode.upper()
    src_file = options.src_file
    target_file = options.target_file

    if mode == 'P':
        print "mode P"
        return "print", "", ""
    elif mode == 'E':
        mode = 'text_input'
    else:
        mode = 'morse_input'

    if src_file == "":
        exit_with_error_msg("Please give input file name")
    elif not _f.exists(src_file):
        exit_with_error_msg("Input file with given name does not exist")

    if target_file == "":
        exit_with_error_msg("Please give output file name")
    # if exists, will be overwritten

    return mode, src_file, target_file
