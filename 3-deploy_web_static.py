#!/usr/bin/python3
""" Bsed on '2-do_deploy_web_static.py' that creates and distributes an archive
    to my web servers.
"""
from fabric.api import run, env, put
dpack = __import__("1-pack_web_static")
ddeploy = __import__("2-do_deploy_web_static")
env.hosts = ['web-01.alexmuthini.tech', 'web-02.alexmuthini.tech']
env.user = 'ubuntu'


def deploy():
    """ Deploys my codebase to my servers."""
    filename = dpack.do_pack()
    if filename is None:
        return False
    try:
        success = ddeploy.do_deploy(filename)
        return success
    except Exception:
        return False
