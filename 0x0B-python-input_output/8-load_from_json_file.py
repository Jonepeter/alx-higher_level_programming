#!/usr/bin/python3
"""Module.




"""
import json


def load_from_json_file(filename):
    """
    function.
    """
    with open(filename) as f:
        return json.load(f)
