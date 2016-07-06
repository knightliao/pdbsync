#!/usr/bin/env python
# coding=utf8
import argparse
import logging

logger = logging.getLogger('pdbsync.cli')


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", dest='debug',
                        help="Enable verbose (debug) logging. Default do not output debug info.")
    args = parser.parse_args()
    return args.debug
