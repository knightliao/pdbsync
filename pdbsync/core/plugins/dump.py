# !/usr/bin/env python
# coding=utf8
import subprocess

from pdbsync.core import logger


class PyDump(object):
    def __init__(self, src_db, dest_db, ignore_tables):
        self.src_db = src_db
        self.dest_db = dest_db
        self.ignore_tables = ignore_tables

    def run(self):
        src_db = self.src_db
        dest_db = self.dest_db
        command = "mysqldump --single-transaction --lock-tables=false -h %s -P %s -u%s -p%s %s" % \
                  (src_db.host, src_db.port, src_db.username, src_db.password, src_db.db_name)

        ignore_table_sql_command = ''
        for ignore_table in self.ignore_tables:
            ignore_table_sql_command += (" --ignore-table=%s.%s " % (src_db.db_name, ignore_table))

        dest_command = " | mysql -h %s -P %s -u%s -p%s %s" % \
                       (dest_db.host, dest_db.port, dest_db.username, dest_db.password, dest_db.db_name)

        command += (ignore_table_sql_command + dest_command)

        logger.debug(command)
        subprocess.check_call(command, shell=True)
