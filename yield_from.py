#!/usr/local/bin/python3.4-32

import code

def print_test():
    send = None
    while True:
        recv = yield send
        print('Recv: {0}'.format(recv))
        send = recv

def deco():
    print('Start...')
    yield from print_test()
    print('End...')

if __name__ == '__main__':
    shell = code.InteractiveConsole(globals())
    shell.interact()
