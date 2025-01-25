#!/usr/bin/python
# -*- coding: utf-8 -*-

import json


class NodeAPI(object):

    def list_nodes(self, *args, **kwargs):
        url = self.base_url + "nodes"
        contents = self.get(url, **kwargs)
        return contents

    def jobs_node(self, id):
        url = self.base_url + "nodes/%s/jobs" % id
        contents = self.get(url)
        return contents

    def print_default_node(
        self,
        id,
        data=None,
        data_b64=None,
        name=None,
        type=None,
        format=None,
        options=None,
    ):
        url = self.base_url + "nodes/%s/print" % id
        contents = self.post(
            url,
            params=dict(
                data=data,
                data_b64=data_b64,
                name=name,
                type=type,
                format=format,
                options=json.dumps(options) if options else None,
            ),
        )
        return contents

    def print_hello_default_node(
        self,
        id,
        type=None,
        format=None,
        options=None,
    ):
        url = self.base_url + "nodes/%s/print_hello" % id
        contents = self.post(
            url,
            params=dict(
                type=type,
                format=format,
                options=json.dumps(options) if options else None,
            ),
        )
        return contents

    def print_printer_node(
        self,
        id,
        printer=None,
        data=None,
        data_b64=None,
        name=None,
        type=None,
        format=None,
        options=None,
    ):
        url = self.base_url + "nodes/%s/printers/print" % id
        contents = self.post(
            url,
            params=dict(
                printer=printer,
                data=data,
                data_b64=data_b64,
                name=name,
                type=type,
                format=format,
                options=json.dumps(options) if options else None,
            ),
        )
        return contents

    def print_hello_printer_node(
        self, id, printer=None, type=None, format=None, options=None
    ):
        url = self.base_url + "nodes/%s/printers/print_hello" % id
        contents = self.post(
            url,
            params=dict(
                printer=printer,
                type=type,
                format=format,
                options=json.dumps(options) if options else None,
            ),
        )
        return contents


class Node(dict):
    pass
