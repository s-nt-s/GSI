import subprocess
import sys

def run(*args, **kargv):
    output = subprocess.check_output(args, **kargv)
    output = output.decode(sys.stdout.encoding)
    return output
