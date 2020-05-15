#!c:\users\shivam\pycharmprojects\site_checker\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'site-checker','console_scripts','checker'
__requires__ = 'site-checker'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('site-checker', 'console_scripts', 'checker')()
    )
