import argparse
import string
from random import choices


def passgen(length, digit, lower, upper, pun):
    pool = ''
    if digit:
        pool += string.digits
    if pun:
        pool += string.punctuation
    if lower:
        pool += string.ascii_lowercase
    if upper:
        pool += string.ascii_uppercase
    if not (upper and lower and pun and digit):  # if pool == '':
        pool += string.ascii_letters

    return ''.join(choices(pool, k=length))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Password generator',
                                     description='Simple program generating '
                                                 'standard passwords.')

    parser.add_argument('length', type=int, help='Length of password')
    # parser.add_argument('-a', '--ascii', help='ascii', action='store_true')
    parser.add_argument('--verbose', '-v', action='count', default=0)
    parser.add_argument('-l', '--lower', help='lowercase', action='store_true')
    parser.add_argument('-u', '--upper', help='uppercase', action='store_true')
    parser.add_argument('-p', '--pun', help='punctuation', action='store_true')
    parser.add_argument('-d', '--digit',
                        help='digit password', action='store_true')

    args = parser.parse_args()
    print(args)
    pwd = passgen(args.length, args.digit, args.lower, args.upper, args.pun)
    print(pwd)

