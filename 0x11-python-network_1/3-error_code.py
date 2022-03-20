#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
'''

if __name__ == '__main__':
    import urllib.request
    from sys import argv

    r = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(r) as response:
            html = response.read()
        print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
