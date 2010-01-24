
import os,sys
import shutil

def p(options,buildout):

    src  = os.path.join(options['location'], 'sbin')
    dst  = os.path.join(options['location'], 'bin')
    if os.path.exists(src):
        if os.path.exists(dst):
            shutil.rmtree(dst)
        os.rename(src, dst)



