# !/usr/bin/env python
# coding=utf8


class PdbSyncCore(object):
    def __init__(self, dbs):
        self.dbs = dbs

    def _pre(self):
        pass

    def _after(self):
        pass

    def run(self):
        for db in self.dbs:
            logger.info("db: %s" % db)

            pydump = PyDump(db.src, db.dest)
            pydump.run()
