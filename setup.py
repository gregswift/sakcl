#!/usr/bin/python

from setuptools import setup

import sys
sys.path.insert(0, '.')

NAME = "sakcl"
SHORT_DESC = "SSH AuthorizedKeysCommand Lookup tool"

if __name__ == "__main__":
 
    setup(
        name = NAME,
        version = '0.1.0',
        author = 'Greg Swift',
        author_email = 'gregswift@gmail.com',
        url = 'https://github.com/gregswift/%s'.format(NAME),
        license = 'ASLv2',
        description = SHORT_DESC,
        install_requires = ['requests', 'configobj'],
        scripts = [NAME],
    )
