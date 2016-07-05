# !/usr/bin/env python
# coding=utf8
import subprocess

from pdbsync.core import logger


class PyExecute(object):
    def __init__(self, dest_db):
        self.dest_db = dest_db

    def run(self, sql):
        dest_db = self.dest_db
        command = "mysql -h %s -P %s -u%s -p%s --default-character-set=utf8 < %s" % \
                  (dest_db.host, dest_db.port, dest_db.username, dest_db.password, sql)

        logger.info(command)
        subprocess.Popen(command, shell=True)
