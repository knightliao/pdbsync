# !/usr/bin/env python
# coding=utf8
from pdbsync.core import logger
from pdbsync.core.plugins.db_create import DbCreateExecutor
from pdbsync.core.plugins.dump import PyDump
from pdbsync.core.plugins.execute import PyExecute


class PdbSync(object):
    def __init__(self, dbs):
        self.dbs = dbs

    def _pre(self, db_data):
        execute = DbCreateExecutor(db_data)
        execute.run()

    def _after(self, db_data):
        if db_data.after_sql:
            execute = PyExecute(db_data)
            execute.run(db_data.after_sql)

    def _run(self, src_db, dest_db, ignore_tables):
        dump = PyDump(src_db, dest_db, ignore_tables)
        dump.run()

    def run(self):

        for db in self.dbs:
            logger.info("================ db: %s =======================" % db)

            self._pre(db.dest)
            self._run(db.src, db.dest, db.ignore_tables)
            self._after(db.dest)
