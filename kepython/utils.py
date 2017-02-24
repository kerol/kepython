# -*- coding: utf-8 -*-
"""
    utils
    ~~~~~

    Python utils.

    :copyright: (c) 2017 by Kerol Gao.
    :license: Apache License.
"""

import struct
import socket


def ip2int(ip):
    return struct.unpack("!I",socket.inet_aton(ip))[0]


def int2ip(i):
    return socket.inet_ntoa(struct.pack("!I",i))

def logger():
    " logging print "
    import logging
    logger = logging.getLogger('logger_name')
    logger.setLevel(logging.DEBUG)
    # file log
    fh = logging.FileHandler('logger_file.log')
    fh.setLevel(logging.DEBUG)
    # console log
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

