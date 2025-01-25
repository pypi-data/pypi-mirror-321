#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from .job import JobAPI
from .node import NodeAPI

BASE_URL = "https://print.bemisc.com/api/"
""" The default base URL to be used when no other
base URL value is provided to the constructor """


class API(appier.API, JobAPI, NodeAPI):
    """
    Implementation of the Colony Print API specification
    for a simplified python client usage.
    """

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.base_url = appier.conf("PRINT_BASE_URL", BASE_URL)
        self.key = appier.conf("PRINT_KEY", None)
        self.base_url = kwargs.get("base_url", self.base_url)
        self.key = appier.conf("key", self.key)

    def build(
        self,
        method,
        url,
        data=None,
        data_j=None,
        data_m=None,
        headers=None,
        params=None,
        mime=None,
        kwargs=None,
    ):
        auth = kwargs.pop("auth", True)
        if auth and self.key:
            headers["X-Secret-Key"] = self.key

    def ping(self):
        url = self.base_url + "ping"
        contents = self.get(url, auth=False)
        return contents


class Ping(dict):
    pass
