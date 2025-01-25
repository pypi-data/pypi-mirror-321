#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import base64
import pprint

import appier
import colony_print


def print(id, printer=None):
    api = colony_print.API()
    if printer:
        return api.print_hello_printer_node(id, printer)
    else:
        return api.print_hello_default_node(id)


def save(id, printer=None):
    api = colony_print.API()
    options = dict(send_email=False, save_output=True)
    if printer:
        result = api.print_hello_printer_node(id, printer, options=options)
    else:
        result = api.print_hello_default_node(id, options=options)

    job_id = result["id"]
    result = api.wait_job(job_id)
    if not "output_data" in result:
        raise appier.OperationalError(message="No output data in result")

    data_b64 = result["output_data"]
    data = base64.b64decode(data_b64)
    with open("output.pdf", "wb") as file:
        file.write(data)

    return result


if __name__ == "__main__":
    node = appier.conf("NODE", None)
    printer = appier.conf("PRINTER", None)
    save_pdf = appier.conf("SAVE_PDF", False, cast=bool)

    if not node:
        raise appier.OperationalError(message="No node defined")

    result = save(node, printer=printer) if save_pdf else print(node, printer=printer)
    pprint.pprint(result)
else:
    __path__ = []
