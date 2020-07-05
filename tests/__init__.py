#!/usr/bin/env python

import os
import sys

temp_dir = os.path.split(os.path.realpath(__file__))[0]
dir_list = temp_dir.split("/")
root_dir = "/".join(dir_list[0:dir_list.index("tests")]) + './'

if root_dir not in sys.path:
    sys.path.insert(0, root_dir)


def setup():
    print "UT setup"


def teardown():
    print "UT teardown"
