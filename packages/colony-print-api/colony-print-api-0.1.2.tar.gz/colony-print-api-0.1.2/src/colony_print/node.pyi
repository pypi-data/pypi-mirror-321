#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import NotRequired, Sequence, TypedDict

from .job import JobsResult, PrintResult

class Node(TypedDict):
    name: str
    mode: str
    location: NotRequired[str]
    node_printer: NotRequired[str]
    engines: Sequence[str]

class NodeAPI:
    def list_nodes(self) -> Sequence[Node]: ...
    def jobs_node(self, id: str) -> JobsResult: ...
    def print_default_node(
        self,
        id: str,
        data: str | None = None,
        data_b64: str | None = None,
        name: str | None = None,
        type: str | None = None,
        format: str | None = None,
        options: dict | None = None,
    ) -> PrintResult: ...
    def print_hello_default_node(
        self,
        id: str,
        type: str | None = None,
        format: str | None = None,
        options: dict | None = None,
    ) -> PrintResult: ...
    def print_printer_node(
        self,
        id: str,
        printer: str | None = None,
        data: str | None = None,
        data_b64: str | None = None,
        name: str | None = None,
        type: str | None = None,
        format: str | None = None,
        options: dict | None = None,
    ) -> PrintResult: ...
    def print_hello_printer_node(
        self,
        id: str,
        printer: str | None = None,
        type: str | None = None,
        format: str | None = None,
        options: dict | None = None,
    ) -> PrintResult: ...
