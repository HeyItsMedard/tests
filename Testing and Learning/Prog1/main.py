import argparse
import os

parser = argparse.ArgumentParser(prog="Lister", description="Lists files only by extension if given")

parser.add_argument('folder')
parser.add_argument('-e', '--extension', nargs="+")
parser.add_argument('-v', '--verbose', action='store_true', help="display how many lines a file has if it is possible")

args = parser.parse_args()

def how_many_lines(file):
  try:
    with open(file) as f:
      return len(f.readlines())
  except:
    return '?'

for file in os.scandir(args.folder):
    (name, ext) = os.path.splitext(file)
    ext = ext.replace('.', '')
    if not args.extension or ext in args.extension:
        if args.verbose:
          print(file.name, how_many_lines(os.path.abspath(file)))
        else:
          print(file.name)
