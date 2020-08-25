#!/usr/bin/python3
"""
Send request and dysplay X-var
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
