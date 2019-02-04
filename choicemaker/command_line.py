import argparse
import random
import os.path
import os
import sys

DEFAULT_FILE='default_file.txt'

def main():

    default_file=get_default_file()
	
    parser=argparse.ArgumentParser()
	
    parser.add_argument('--file','-f',default=default_file,
                        help='Select the FILE containing your options, this is a one-time modification of your choices file.')
    parser.add_argument('--default','-d',default=None,
                        help='Change the default choices file.')
    parser.add_argument('--check','-c',action='store_true',
                        help='Check the default choices file.')
    parser.add_argument('--reset','-r',action='store_true',
                        help='Reset the default file (IRREVERSIBLE!).')
    parser.add_argument('--list','-l',action='store_true',
                        help='List choices.')
    args=parser.parse_args()

    if args.default!=None:
        set_default_file(args.default)
        return

    if args.check:
        print(default_file)
        return

    if args.reset:
        reset_default_file()
        return

    file_name=os.path.expanduser(args.file)

    # 1) needs to read some choice.txt file or something
    # 2) store the options and count them
    choices=[]

    try:
        with open(file_name,"r") as f:
            for line in f:
                choices.append(line)

    except FileNotFoundError:
        print('no such file, please create it manually or check the name')
        print('file name tried :')
        print(args.file)
        print('\n')
        return

    if args.list:
        for line in choices:
            print(line)
        return

    # 3) select one at random
    selection=random.randint(0,len(choices)-1)
    # 4) print the result
    print(choices[selection])


def set_default_file(file):
    f=open(DEFAULT_FILE,'w')
    f.write(file)


def get_default_file():
    try:
        f=open(DEFAULT_FILE,'r')
        return f.read()
    except FileNotFoundError:
        return '~/.choices.txt'


def reset_default_file():
    try:
        os.remove(DEFAULT_FILE)
        return
    except FileNotFoundError:
        return


#main(argparse.ArgumentParser())
