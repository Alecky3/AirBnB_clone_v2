#!/usr/bin/python3
""" Generates a .tgz archive from the contents of the web_statis folder
    of AirBnB_clone using the function 'do_pack'.
"""
from fabric.api import local
from os.path import isdir
from datetime import datetime


def do_pack():
    """ Generates a tgz archive file."""
    try:
        date_now = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir('versions'):
            local('mkdir versions')
        filename = 'versions/web_static_{0}.tgz'.format(date_now)
        local('touch {}'.format(filename))
        local('tar -cvzf {} web_static'.format(filename))
        return filename
    except:
        return None
