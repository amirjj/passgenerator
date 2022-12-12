import argparse


def passgen():
    parser = argparse.ArgumentParser(prog='Password generator',
                                     description='A Simple program generating '
                                                 'standard passwords',
                                     epilog='Help text')
    parser.add_argument('-a', '--ascii')
    print(parser)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Password generator',
                                     description='Simple program generating '
                                                 'standard passwords.')

    parser.add_argument('length', type=int, help='Length of password')
    parser.add_argument('--foo', action='store_false')
    parser.add_argument('-l', '--lower', help='lowercase', action='store_true')
    parser.add_argument('-u', '--upper', help='uppercase', action='store_true')
    parser.add_argument('-p', '--pun', help='punctuation', action='store_true')
    parser.add_argument('-d', '--digit',
                        help='digit password', action='store_true')

    args = parser.parse_args()

    print(args)

