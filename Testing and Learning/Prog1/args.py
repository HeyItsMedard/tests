# import sys, os

# print(sys.argv)

# def list(p):
#     print(os.listdir(p))

# list(sys.argv[1])

import argparse

parser = argparse.ArgumentParser(prog='LISTerine', description="List files in a given folder")
parser.add_argument('folder')
parser.add_argument('-r', '--recursive', action="store_true")
# parser.add_argument('-v', '--verbose', action="store_true")
# parser.add_argument('-d', '--depth', type=int, required=True)
# parser.add_argument('-t', '--threads', choices=[1, 2], type=int)


# args = parser.parse_args()

# print(type(args.depth))
