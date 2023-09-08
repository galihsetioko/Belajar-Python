# Galih Setioko

import sys , string

def generatePass(value:string) -> string:
    pw = list(value.capitalize())
    pw_string = ''
    for index, data in enumerate(pw):
        if index != 0 and data == 'a' or data == 'A':
           pw_string += '4'
        elif index != 0 and data == 's' or data == 'S':
           pw_string += '5'
        elif index != 0 and data == 'o' or data == 'O':
           pw_string += '0'
        elif index != 0 and data == 'g' or data == 'G':
           pw_string += '6'
        else :
            pw_string += data
    print(pw_string)

if __name__ == '__main__':
    try:
        input = sys.argv[1]
        print('\n')
        generatePass(input)
        print('\n')
    except IndexError:
        print('[-] Error program..')