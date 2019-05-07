# from subprocess import Popen, PIPE

# def execute():
#     process = Popen(
#             ["python", "testprocesss.py"],
#             cwd=None,
#             shell=False,
#             close_fds=True,
#             stdout=PIPE,
#             stderr=PIPE,
#             bufsize=1
#         )
    
#     errors = []
#     # read error lines from the PIPE
#     for line in process.stderr.readline():
#         errors.append(line)
    
#     out = ' '.join(errors)

#     print out

#     # print process.stdout.readline()
#     # print process.stderr.readline().encode('UTF-8')

# execute()

import requests
import json 
from requests.utils import quote
try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode


def get_url():
    url = 'https://api.stackexchange.com/2.2/search?'
    params = {
        'order':'desc', 
        'sort':'relevance', 
        'tagged':'python', 
        'intitle': 'ZeroDivisionError: integer division or modulo by zero',
        'site': 'stackoverflow'
        }

    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    url = urlparse.urlunparse(url_parts).strip()

    return url

r = requests.get(get_url())
print(json.dumps(r.json(), indent=4, sort_keys=True))

######


