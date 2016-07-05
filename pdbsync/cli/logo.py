#!/usr/bin/env python
# coding=utf8
import os

import pdbsync


# http://www.kammerl.de/ascii/AsciiSignature.php

def print_logo():
    logo_path = os.path.join(os.path.dirname(pdbsync.__file__), "logo.txt")
    try:
        with open(logo_path, 'r') as fin:
            print fin.read()
    except:
        pass
