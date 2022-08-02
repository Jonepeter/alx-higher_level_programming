#!/usr/bin/python3
''' Module Input Output'''
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    a = load_from_json_file("add_item.json")
except Exception:
    a = []
a.extend(sys.argv[1:])
save_to_json_file(a, "add_item.json")
