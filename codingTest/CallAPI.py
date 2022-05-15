import sys
import requests
import json

def main(argv):
    url = "http://challenge-server.code-check.io/api/hash"
    params={"q":argv[0]}
    r = requests.get(url,params)
    res=r.json()['hash']
    print(res)

if __name__ == '__main__':
    main(sys.argv[1:])