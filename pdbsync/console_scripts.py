#!/usr/bin/env python
# coding=utf8

import os
import sys
import time

import pdbsync
from pdbsync.cli import argument_parser
from pdbsync.cli.config_parser import PdbSyncConfigParser
from pdbsync.cli.log import make_logging
from pdbsync.core.sync import PdbSync

pdbsync_file = 'pdbsync.json'


def main():
    sys.path.insert(0, os.getcwd())

    debug = argument_parser()

    # log
    make_logging(debug)
    print "pdbsync version %s " % pdbsync.__version__
    time.sleep(1)

    # parser
    root_config = PdbSyncConfigParser.do(pdbsync_file)

    if root_config:
        sync = PdbSync(root_config.dbs)
        sync.run()


if __name__ == "__main__":
    main()
