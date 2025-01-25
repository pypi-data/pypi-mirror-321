#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Mapping, NotRequired, TypedDict

class JobResult(TypedDict):
    handler: str
    result: str
    receivers: NotRequired[list[str]]
    output_data: NotRequired[str]

class JobInfo(TypedDict):
    name: str
    node_id: str
    printer: str | None
    status: str | None
    result: NotRequired[JobResult]

JobsResult = Mapping[str, JobInfo]

class PrintResult(TypedDict):
    id: str
    name: str
    node_id: str
    printer: str | None
    data_length: int

class JobAPI:
    def list_jobs(self) -> JobsResult: ...
    def get_job(self, id: str) -> JobInfo: ...
    def wait_job(
        self, id: str, sleep: float = ..., iterations: int = ...
    ) -> JobResult: ...
