#!/usr/bin/env python
# coding=utf8

import os
import sys
import time

import pdbsync
from pdbsync.cli.config_parser import PdbSyncConfigParser
from pdbsync.cli.log import make_logging

pdbsync_file = 'pdbsync.json'


def main():
    sys.path.insert(0, os.getcwd())

    # log
    make_logging(True)
    print "pdbsync version %s " % pdbsync.__version__
    time.sleep(1)

    # parser
    PdbSyncConfigParser.do(pdbsync_file)


if __name__ == "__main__":
    main()
