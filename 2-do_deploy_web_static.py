#!/usr/bin/python3
"""
Distributes an archive to your web servers,
using the function do_deploy
"""
from os.path import exists
from fabric.api import task
from fabric.api import local
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ['100.25.13.203', '34.201.61.187']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, '/tmp/')
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'
            .format(timestamp))
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C '
            '/data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))
        run('sudo rm /tmp/web_static_{}.tgz'
            .format(timestamp))
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* '
            '/data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))
        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'
            .format(timestamp))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/web_static_{}/ '
            '/data/web_static/current'
            .format(timestamp))
    except Exception as e:
        print(e)
        return False
    return True

