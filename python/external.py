import sys
import subprocess

def system(cmd):
    """
    Invoke a shell command.
    :returns: A tuple of output, err message and return code
    """
    ret = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=False)
    out, err = ret.communicate()
    return out, err, ret.returncode

if __name__ == "__main__":

    cmd = sys.argv[1:]
    print "cmd=",cmd
    out, err, retcode = system(cmd)
    print "out=", out
    print "err=",err
    print "retcode=", retcode
