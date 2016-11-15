#!/usr/bin/python
# Filename: zip.py
import os
import time

source = ['/home/m/python/test.py', '/home/m/python']
target_dir = '/home/m/python/'

target = target_dir + time.strftime('%Y%m%d') + '.zip'

zip_command = 'zip -qr %s %s' %(target, ' '.join(source))

if os.system(zip_command) == 0:
    print "Successful back up to", target
else:
    print 'Failed'

print ' '.join(source)
print target
