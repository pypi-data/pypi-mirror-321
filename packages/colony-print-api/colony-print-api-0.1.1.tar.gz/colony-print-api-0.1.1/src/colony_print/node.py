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
        params = dict()
        if not data == None:
            params["data"] = data
        if not data_b64 == None:
            params["data_b64"] = data_b64
        if not name == None:
            params["name"] = name
        if not type == None:
            params["type"] = type
        if not format == None:
            params["format"] = format
        if not options == None:
            params["options"] = json.dumps(options)
        contents = self.post(
            url,
            params=params,
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
        params = dict()
        if not type == None:
            params["type"] = type
        if not format == None:
            params["format"] = format
        if not options == None:
            params["options"] = json.dumps(options)
        contents = self.post(
            url,
            params=params,
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
        params = dict()
        if not printer == None:
            params["printer"] = printer
        if not data == None:
            params["data"] = data
        if not data_b64 == None:
            params["data_b64"] = data_b64
        if not name == None:
            params["name"] = name
        if not type == None:
            params["type"] = type
        if not format == None:
            params["format"] = format
        if not options == None:
            params["options"] = json.dumps(options)
        contents = self.post(
            url,
            params=params,
        )
        return contents

    def print_hello_printer_node(
        self, id, printer=None, type=None, format=None, options=None
    ):
        url = self.base_url + "nodes/%s/printers/print_hello" % id
        params = dict()
        if not printer == None:
            params["printer"] = printer
        if not type == None:
            params["type"] = type
        if not format == None:
            params["format"] = format
        if not options == None:
            params["options"] = json.dumps(options)
        contents = self.post(
            url,
            params=params,
        )
        return contents


class Node(dict):
    pass
