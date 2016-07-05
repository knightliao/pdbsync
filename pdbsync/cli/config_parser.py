# !/usr/bin/env python
# coding=utf8
import json
import traceback

from pdbsync.cli import logger


class PdbSyncConfigParser(object):
    @classmethod
    def do(cls, config_file_path):
        with open(config_file_path, 'r') as fin:

            try:
                config_data = json.load(fin)
            except:
                logger.error("%s not well formed \n%s" % (config_file_path, traceback.format_exc()))
                return None

            logger.info(config_data)
