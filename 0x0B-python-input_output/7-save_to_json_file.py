#!/usr/bin/python3
"""
Contain save_to_json_file function
"""

import json


def save_to_json_file(my_obj, filename):
    """write Object to a text file using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
