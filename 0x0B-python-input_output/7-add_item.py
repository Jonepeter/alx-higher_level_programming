#!/usr/bin/python3
''' Module Input Output'''
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    l = load_from_json_file("add_item.json")
except Exception:
    l = []
l.extend(sys.argv[1:])
save_to_json_file(l, "add_item.json")
