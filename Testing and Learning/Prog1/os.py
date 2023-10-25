import os

p = os.path.join('demo', 'stuff', 'existing', 'movie.mp4')
# print(p)
# print(os.path.isdir(p))
# print(os.path.isfile(p))
# print(os.path.exists(p))

# for file in os.listdir('demo'):
#     print(file, os.path.isfile(os.path.join('demo', file)))

# for file in os.scandir('demo'):
#     print(file.name, file.is_file())

# print(os.getcwd())
# print(os.listdir())
# os.chdir('demo')
# os.chdir('..')
# print(os.getcwd())
# print(os.listdir())

# os.rename('asd', 'demo')

# os.remove('demo/file-sample_100kB')

def copy(source, target):
  if os.name != 'nt':
    os.system(f'cp {source} {target}')
  else:
    os.system(f'copy {source} {target}')

# copy('os.py', 'demo2.py')

def list(root):
  for path_like in os.listdir(root):
    sub_path = os.path.join(root, path_like)
    if os.path.isdir(sub_path):
      list(sub_path)
    else:
      print(root, path_like)

# list('demo')

# for (root, folders, files) in os.walk('demo'):
#   print(root, files)
