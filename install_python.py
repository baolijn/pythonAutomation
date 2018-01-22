# coding = utf-8

import os
import sys

if os.getuid() == 0:
    pass
else:
    print 'current user is not root, please use root to execute this scripts'	
    sys.exit(1)

version = raw_input('Please choose the version you want(2.7/3.5)')
if version == '2.7':
    url = 'https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz'
elif version == '3.5':
    url = 'https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz'
else:
    print 'Your version is not correct, Please choose 2.7 or 3.5'
    sys.exit(1)

cmd = 'wget '+url
res = os.system(cmd)
if res != 0:
    print 'Download failed, please check you network'
    sys.exit(1)

if version == '2.7':
    package_name = 'Python-2.7.12'
else:
    package_name = 'Python-3.5.2'

cmd = 'tar xf '+package_name+'.tgz'
res = os.system(cmd)
if res != 0:
    print 'unzip failed'
    sys.exit(1)

cmd = 'cd ' + package_name + ' && ./configure --prefix=/usr/local/python && make && make install'
res = os.system(cmd)

if res != 0:
    print 'install python failed'
    sys.exit(1)
