# !/usr/bin/env python
# coding=utf8
import subprocess

from pdbsync.core import logger


class PyExecute(object):
    def __init__(self, dest_db):
        self.dest_db = dest_db

    def run(self, sql, with_db=True):
        dest_db = self.dest_db

        if with_db:
            command = "mysql -h %s -P %s -u%s -p%s %s --default-character-set=utf8 < %s" % \
                      (dest_db.host, dest_db.port, dest_db.username, dest_db.password, dest_db.db_name, sql)
        else:
            command = "mysql -h %s -P %s -u%s -p%s --default-character-set=utf8 < %s" % \
                      (dest_db.host, dest_db.port, dest_db.username, dest_db.password, sql)
        logger.info(command)
        subprocess.check_call(command, shell=True)
