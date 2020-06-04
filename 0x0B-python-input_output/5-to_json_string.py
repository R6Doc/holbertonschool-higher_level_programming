#!/usr/bin/python3
"""
Contain to_json_string fundtion
"""

import json


def to_json_string(my_obj):
    """return JSON representation of an object"""
    return json.dumps(my_obj)
