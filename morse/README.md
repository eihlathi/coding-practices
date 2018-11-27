# MORSE CODE CONVERTER

These python scripts make morse conversion from text to morse or vice versa. Input is read from fíle and output printed to another.

## Implementation

In morse table space is used as separator between characters and '/' betweeen words.

Illegal characters in both directions are ignored and notified with prints to user, but they are not stopping execution. So all legal chars are translated. Also scandic characters are included in morse table if python3 is used, with python2 those are just ignored.

Main module is for current command line and file spesified implementation. Variables input_content and output_content can be used in implementations with different interfaces.

Doxygen documentation can be generated with attached configuration file. However all wanted code is not coming to documentation. Documentation is not included. 

## Usage

Put wanted text to input file. Run script:
```
python morse_main.py

This script converts english to morse code OR morse to english.
It reads input from file and writes output to file. Files and scripts must be in same folder.
File names and direction of conversion is asked from user. Or if just wanted to print morse table.

Give action: 'P'/'p': print morse table
'E'/'e': convert english -> morse code,
anything else: convert morse code->english
e
Give input file name:  ace_of_spades.txt
Give output file name: aos_morse.txt```
```
Check output file content.

## Testing

Basically testing is done manually, defining input in output file, running script, checking possible error prints (mostly there is told not supported chars, but sometimes some fatal error) and output file. Converting back and checking against original file can be done to see if contents are the same.

I copied some text from internet for testing. With https://morsecode.scphillips.com/translator.html I feeded text there and to own script, then converted back for comparing. It is difficult to compare when all is in same line, so I cutted output files manually as lines to see the difference. Seemed to work fine in my tests except chars ' and ! missing from own implementation. Explanation: web converted has enlarged set of morse codes (for example scandic):  https://morsecode.scphillips.com/morse.html

Adding some more morse codes it would be possible to compare automatically results with that common converter. Same text feeded to both and results compared.

Some test files are found in /Tests folder.

One idea was to feed automatically text to  https://morsecode.scphillips.com/translator.html with python selenium script (morse_web_conversion.py in /Tests folder). Input and output are working but not taken actuall in test use. Should be easy to feed same file inputs/outputs there. https://docs.python.org/2/library/filecmp.html could be comparing output (just True/False result).

Tested in win10 and linux.
