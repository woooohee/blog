#!c:\work\myvenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ndg-httpsclient==0.4.0','console_scripts','ndg_httpclient'
__requires__ = 'ndg-httpsclient==0.4.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ndg-httpsclient==0.4.0', 'console_scripts', 'ndg_httpclient')()
    )
