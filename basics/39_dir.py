from os import mkdir, path, chdir, rename, rmdir, unlink
from shutil import copytree, move, rmtree

dir_name = path.join(path.dirname(__file__), 'new_dir')
mkdir(dir_name)
chdir(path.dirname(__file__))
# rmdir(dir_name)
# rename('new_dir', 'new_name_dir')

copytree('new_dir', 'copy_new_dir')
# move()
rmtree('new_dir')

newfile = open('newfile', 'w')
# rename(src,dest)
# unlink(file)
