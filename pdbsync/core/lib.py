#!/usr/bin/env python
# coding=utf8
import importlib


def auto_str(cls):
    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls


def import_from_file(class_path):
    r_index = class_path.rfind('.')
    module = importlib.import_module(class_path[0:r_index])
    my_class = getattr(module, class_path[r_index + 1:])
    return my_class


def get_value_from_map(cur_map, cur_key, default=None):
    return cur_map[cur_key] if cur_key in cur_map else default
