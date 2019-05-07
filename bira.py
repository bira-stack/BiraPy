from queue import Queue
from subprocess import PIPE, Popen
from threading import Thread
import shlex
import os
import requests
import json 
from requests.utils import quote
try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode


def read(pipe, funcs):
    for line in iter(pipe.readline, b''):
        for func in funcs:
            func(line.decode("utf-8"))
    pipe.close()

def write(get):
    for line in iter(get, None):
        print(line.strip('\n'))


def execute(command):

    process = Popen(
        ["python", command],
        cwd=None,
        shell=False,
        close_fds=True,
        stdout=PIPE,
        stderr=PIPE,
        bufsize=1
    )

    output, errors = [], []
    pipe_queue = Queue() 

    stdout_thread = Thread(target=read, args=(process.stdout, [pipe_queue.put, output.append]))
    stderr_thread = Thread(target=read, args=(process.stderr, [pipe_queue.put, errors.append]))

    writer_thread = Thread(target=write, args=(pipe_queue.get,)) 

    for thread in (stdout_thread, stderr_thread, writer_thread):
        thread.daemon = True
        thread.start()

    process.wait()

    for thread in (stdout_thread, stderr_thread):
        thread.join()

    pipe_queue.put(None)

    output = ' '.join(output)
    errors = ' '.join(errors)

    return errors

def get_error_message(error):
    if error == '':
        return None
    elif any(e in error for e in ["KeyboardInterrupt", "SystemExit", "GeneratorExit"]): # Non-compiler errors
        return None
    else:
        return error.split('\n')[-2].strip()

def get_api_url(error_message):
    intitle = error_message
    url = 'https://api.stackexchange.com/2.2/search?'
    params = {
        'order':'desc', 
        'sort':'relevance', 
        'tagged':'python',
        'site': 'stackoverflow', 
        'intitle': intitle
        }

    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    url = urlparse.urlunparse(url_parts).strip()

    return url

# r = requests.get(get_api_url(get_error_message(execute("testprocesss.py"))))
# print(json.dumps(r.json(), indent=4, sort_keys=True))

