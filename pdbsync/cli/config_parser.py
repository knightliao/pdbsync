# !/usr/bin/env python
# coding=utf8
import json
import traceback

from pdbsync.cli import logger
from pdbsync.core.constants import ROOT_SETTINGS, ROOT_DBS, SETTINGS_BASESRC, SETTINGS_BASEDEST, DB_DATA_HOST, \
    DB_DATA_PORT, DB_DATA_USERNAME, DB_DATA_PASSWORD, DB_SRC, DB_DEST, DB_DATA_NAME, DB_DATA_PRE_SQL, DB_DATA_AFTER_SQL
from pdbsync.core.lib import auto_str, get_value_from_map


@auto_str
class PdbSyncConfig(object):
    def __init__(self, settings, dbs):
        self.settings = settings
        self.dbs = dbs


#
# 基础配置,用于继承
#
@auto_str
class PdbSyncConfigSettings(object):
    def __init__(self, basesrc, basedest):
        self.basesrc = basesrc
        self.basedest = basedest


#
# 数据库(源+目标)
#
class PdbSyncConfigDb(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def __repr__(self):
        return "%s -> %s" % (self.src, self.dest)


#
# 数据库配置
#
class PdbSyncConfigDbData(object):
    def __init__(self, host, port, username, password, db_name, pre_sql, after_sql):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name
        self.pre_sql = pre_sql
        self.after_sql = after_sql

    def set_value_if_none(self, base_db):
        if base_db:
            if not self.host and base_db.host:
                self.host = base_db.host
            if not self.port and base_db.port:
                self.port = base_db.port
            if not self.username and base_db.username:
                self.username = base_db.username
            if not self.password and base_db.password:
                self.password = base_db.password
            if not self.db_name and base_db.db_name:
                self.db_name = base_db.db_name

    def __repr__(self):
        return "(%s:%s:%s:****)" % (self.host, self.port, self.username)

    def verify(self):
        if not self.host:
            logger.warn(str(self) + " lost host")
            return False
        if not self.port:
            logger.warn(str(self) + " lost port")
            return False
        if not self.username:
            logger.warn(str(self) + " lost username")
            return False
        if not self.password:
            logger.warn(str(self) + "  lost password")
            return False
        if not self.db_name:
            logger.warn(str(self) + " lost db_name")
            return False
        return True


class PdbSyncConfigParser(object):
    @classmethod
    def _parse_dbs(cls, dbs, settings):
        cur_dbs = []
        if dbs:
            for db in dbs:

                src = get_value_from_map(db, DB_SRC)
                dest = get_value_from_map(db, DB_DEST)

                cur_src = None
                if src is not None:
                    cur_src = cls._parse_db_data(src)
                    cur_src.set_value_if_none(settings.basesrc)
                    if not cur_src.verify():
                        break

                cur_dest = None
                if dest is not None:
                    cur_dest = cls._parse_db_data(dest)
                    cur_dest.set_value_if_none(settings.basedest)
                    if not cur_dest.verify():
                        break

                if cur_src and cur_dest:
                    cur_db = PdbSyncConfigDb(cur_src, cur_dest)
                    cur_dbs.append(cur_db)

        return cur_dbs

    @classmethod
    def _parse_db_data(cls, db_data):
        host = get_value_from_map(db_data, DB_DATA_HOST)
        port = get_value_from_map(db_data, DB_DATA_PORT)
        username = get_value_from_map(db_data, DB_DATA_USERNAME)
        password = get_value_from_map(db_data, DB_DATA_PASSWORD)
        db_name = get_value_from_map(db_data, DB_DATA_NAME)
        pre_sql = get_value_from_map(db_data, DB_DATA_PRE_SQL)
        after_sql = get_value_from_map(db_data, DB_DATA_AFTER_SQL)
        return PdbSyncConfigDbData(host, port, username, password, db_name, pre_sql, after_sql)

    @classmethod
    def _parse_settings(cls, settings):
        basesrc = get_value_from_map(settings, SETTINGS_BASESRC)
        basedest = get_value_from_map(settings, SETTINGS_BASEDEST)

        cur_basesrc = None
        if basesrc:
            cur_basesrc = cls._parse_db_data(basesrc)
        cur_basedest = None
        if basedest:
            cur_basedest = cls._parse_db_data(basedest)
        return PdbSyncConfigSettings(cur_basesrc, cur_basedest)

    @classmethod
    def _parse_all(cls, config_data):
        settings = get_value_from_map(config_data, ROOT_SETTINGS)
        dbs = get_value_from_map(config_data, ROOT_DBS)

        cur_settings = None
        if settings:
            cur_settings = cls._parse_settings(settings)

        cur_dbs = cls._parse_dbs(dbs, cur_settings)

        root_config = PdbSyncConfig(cur_settings, cur_dbs)
        return root_config

    @classmethod
    def do(cls, config_file_path):
        with open(config_file_path, 'r') as fin:

            try:
                config_data = json.load(fin)
            except:
                logger.error("%s not well formed \n%s" % (config_file_path, traceback.format_exc()))
                return None

            # logger.info(config_data)

            if config_data:
                root_config = cls._parse_all(config_data)
                return root_config
            return None
