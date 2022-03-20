#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
using the module requests
"""
if __name__ == "__main__":
    import requests
    r = requests.get('https://intranet.hbtn.io/status')
    html = r.text
    print('Body response:')
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
