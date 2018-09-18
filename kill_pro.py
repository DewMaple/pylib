import sys

name = sys.argv[1]
print pylib.util.proc.ps_aux_grep(name)
print 'kill them all?[n] y/n.'
yes = raw_input()
if yes == 'yes' or yes == 'y' or yes == 'Y':
    pylib.util.proc.kill(name)
