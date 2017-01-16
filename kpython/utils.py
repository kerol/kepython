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

