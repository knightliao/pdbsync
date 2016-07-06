# !/usr/bin/env python
# coding=utf8
import tempfile

from pdbsync.core.plugins.execute import PyExecute


class DbCreateExecutor(PyExecute):
    def __init__(self, dest_db):
        super(DbCreateExecutor, self).__init__(dest_db)

    def run(self, **kwargs):
        create_sql = "DROP DATABASE IF EXISTS `%s`;\
                        CREATE DATABASE `%s`\
                          DEFAULT CHARACTER SET utf8mb4\
                          COLLATE utf8mb4_unicode_ci;" % (self.dest_db.db_name, self.dest_db.db_name)

        with tempfile.NamedTemporaryFile() as fd:
            fd.write(create_sql)
            fd.flush()
            super(DbCreateExecutor, self).run(fd.name)
