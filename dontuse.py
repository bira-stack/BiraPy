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

r = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=relevance&tagged=python&intitle=ZeroDivisionError%3A%20integer%20division%20or%20modulo%20by%20zero&site=stackoverflow')

print(json.dumps(r.json(), indent=4, sort_keys=True))