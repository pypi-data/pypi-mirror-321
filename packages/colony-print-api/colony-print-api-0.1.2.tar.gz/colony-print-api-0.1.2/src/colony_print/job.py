#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import appier


class JobAPI(object):

    def list_jobs(self, *args, **kwargs):
        url = self.base_url + "jobs"
        contents = self.get(url, **kwargs)
        return contents

    def get_job(self, id):
        url = self.base_url + "jobs/%s" % id
        contents = self.get(url)
        return contents

    def wait_job(self, id, sleep=0.5, iterations=20):
        for _ in range(iterations):
            time.sleep(sleep)
            try:
                job = self.get_job(id)
            except Exception:
                continue
            status = job.get("status", None)
            if not status == "finished":
                continue
            if not "result" in job:
                raise appier.OperationalError(message="No result found")
            return job["result"]

        raise appier.OperationalError(
            message="Maximum iterations reached, no output found"
        )


class JobInfo(dict):
    pass


class JobsResult(dict):
    pass


class PrintResult(dict):
    pass
