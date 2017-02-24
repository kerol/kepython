# -*- coding: utf-8 -*-
"""
    flask
    ~~~~~

    flask framework utils.

    :copyright: (c) 2017 by Kerol Gao.
    :license: Apache License.
"""

from functools import partial

from flask import request, abort, current_app
from qiniu import Auth, put_data


def get_param(key, default=None, type=None, required=False, mapping_key=None):
    """获取request参数
    :param key: 参数名
    :param default: 参数默认值
    :param type: 参数类型
    :param mapping: request.XXXX (args, form, headers, values)
    :param required: 参数是否必须
    """
    mapping = getattr(request, mapping_key, {})
    if required is True and key not in mapping:
        abort(400, "Missing param %s" % key)
    value = mapping.get(key, default)
    if type is not None:
        try:
            value = type(value)
        except ValueError, TypeError:
            abort(400, "Invild param type %s, %s needed" % (key, type))
        except Exception as e:
            abort(500, 'Exception caused')

    return value


request_args = partial(get_param, mapping_key="args")
request_form = partial(get_param, mapping_key="form")
request_values = partial(get_param, mapping_key="values")
request_headers = partial(get_param, mapping_key="headers")


def get_ip():
    if 'X-Forwarded-For' in request.headers:
        return request.headers['X-Forwarded-For'].split(',')[0]
    return request.headers.get('X-Real-Ip') or request.remote_addr


def upload_img(filename, data, config):
    " qiniu upload image"
    config = config or current_app.config
    bucket = config['bucket']
    bucket_url = config['bucket_url']
    access_key = config['access_key']
    secret_key = config['secret_key']

    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket, filename)
    ret, info = put_data(token, filename, data)

    return 'http://%s/%s'%(bucket_url, filename)

