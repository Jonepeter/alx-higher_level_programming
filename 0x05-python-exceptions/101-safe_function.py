#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = fct(*args)
        return (a)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
