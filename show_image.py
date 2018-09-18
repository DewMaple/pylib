from pylib import util

path = util.argv[1]
pylib.util.plt.imshow(path, pylib.util.img.imread(path, rgb = True))