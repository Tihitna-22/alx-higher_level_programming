#!/usr/bin/python3
"""
   takes in a URL, sends a request to the URL and
   displays the body of the response
   If the HTTP status code is greater than or equal to 400, print: Error code:
   followed by the value of the HTTP status code
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
